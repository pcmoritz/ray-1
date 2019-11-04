from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import errno
import glob
import io
import os
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile

if sys.version_info[0] >= 3:
    import urllib.request as urllib_request
else:
    import urllib2 as urllib_request

from setuptools import setup, find_packages, Distribution
import setuptools.command.build_ext as _build_ext

# Ideally, we could include these files by putting them in a
# MANIFEST.in or using the package_data argument to setup, but the
# MANIFEST.in gets applied at the very beginning when setup.py runs
# before these files have been created, so we have to move the files
# manually.

# NOTE: The lists below must be kept in sync with ray/BUILD.bazel.

ray_files = [
    "ray/core/src/ray/thirdparty/redis/src/redis-server",
    "ray/core/src/ray/gcs/redis_module/libray_redis_module.so",
    "ray/core/src/plasma/plasma_store_server",
    "ray/_raylet.so",
    "ray/core/src/ray/raylet/raylet_monitor",
    "ray/core/src/ray/raylet/raylet",
    "ray/dashboard/dashboard.py",
]

# These are the directories where automatically generated Python protobuf
# bindings are created.
generated_python_directories = [
    "ray/core/generated",
]

optional_ray_files = []

ray_autoscaler_files = [
    "ray/autoscaler/aws/example-full.yaml",
    "ray/autoscaler/gcp/example-full.yaml",
    "ray/autoscaler/local/example-full.yaml",
    "ray/autoscaler/kubernetes/example-full.yaml",
    "ray/autoscaler/kubernetes/kubectl-rsync.sh",
]

ray_project_files = [
    "ray/projects/schema.json", "ray/projects/templates/cluster_template.yaml",
    "ray/projects/templates/project_template.yaml",
    "ray/projects/templates/requirements.txt"
]

ray_dashboard_files = [
    "ray/dashboard/client/build/favicon.ico",
    "ray/dashboard/client/build/index.html",
]
for dirname in ["css", "js", "media"]:
    ray_dashboard_files += glob.glob(
        "ray/dashboard/client/build/static/{}/*".format(dirname))

optional_ray_files += ray_autoscaler_files
optional_ray_files += ray_project_files
optional_ray_files += ray_dashboard_files

if "RAY_USE_NEW_GCS" in os.environ and os.environ["RAY_USE_NEW_GCS"] == "on":
    ray_files += [
        "ray/core/src/credis/build/src/libmember.so",
        "ray/core/src/credis/build/src/libmaster.so",
        "ray/core/src/credis/redis/src/redis-server"
    ]

extras = {
    "rllib": [
        "pyyaml", "gym[atari]", "opencv-python-headless", "lz4", "scipy",
        "tabulate"
    ],
    "debug": ["psutil", "setproctitle", "py-spy >= 0.2.0"],
    "dashboard": ["aiohttp", "google", "grpcio", "psutil", "setproctitle"],
    "serve": ["uvicorn", "pygments", "werkzeug", "flask", "pandas"],
    "tune": ["tabulate"],
}

def is_native_windows_or_msys():  # Does NOT return true for WSL, which is considered "Linux"
    return sys.platform == 'msys' or sys.platform == 'win32'

def is_invalid_windows_platform():
    return sys.platform == 'msys' or sys.platform == 'win32' and sys.version_string and 'GCC' in sys.version_string

def makedirs(path, exist_ok):
    # WARNING: path components to create should NOT include ".." components
    # Documentation: https://docs.python.org/3/library/os.html#os.makedirs
    if sys.version_info[:2] >= (3, 2):
        os.makedirs(path, exist_ok=exist_ok)
    else:
        try:
            os.makedirs(path)
        except OSError as ex:
            error_due_to_existing_dir = exist_ok and ex.errno == errno.EEXIST and os.path.isdir(path)
            if not error_due_to_existing_dir:
                raise

def download(url):
    return urllib_request.urlopen(url).read()

def bazel_build(root_dir, build_ext=None):  # Keep this as a global function to make life easier during development
    if is_native_windows_or_msys():
        BUILD_SH = os.getenv('BUILD_SH')
        SYSTEMROOT = os.getenv('SYSTEMROOT')
        if (not BUILD_SH) and SYSTEMROOT and os.path.isfile(os.path.join(SYSTEMROOT, 'System32', 'bash.exe')):
            msg = " ".join([
                "You appear to have Bash from WSL, which Bazel is not compatible with.",
                "To avoid potential problems, please explicitly set the %r environment variable for Bazel."
            ]) % ('BUILD_SH',)
            raise ValueError(msg)

    assert os.path.isabs(root_dir), "need current working directory as an absolute path"

    # TODO(mehrdadn): Is this directory needed anymore?
    makedirs(os.path.join(root_dir, 'build'), exist_ok=True)

    # Note: We are passing in sys.executable so that we use the same
    # version of Python to build pyarrow inside the build.sh script. Note
    # that certain flags will not be passed along such as --user or sudo.
    # TODO(rkn): Fix this.
    pyarrow_url = 'https://s3-us-west-2.amazonaws.com/arrow-wheels/3a11193d9530fe8ec7fdb98057f853b708f6f6ae/index.html'
    subprocess.check_call([
        sys.executable, '-m', 'pip', 'install', '-q', 'pyarrow==0.14.0.RAY',
        '--find-links', pyarrow_url,
        '--target', os.path.join(root_dir, 'python', 'ray', 'pyarrow_files')
    ])
    if (3, 6) <= sys.version_info[:2] <= (3, 7):
        pickle5_backport_url = 'https://github.com/pitrou/pickle5-backport/archive/5186f9ca4ce55ae530027db196da51e08208a16b.zip'
        pickle5_dir = os.path.join(root_dir, 'python', 'ray', 'pickle5_files')
        work_dir = tempfile.mkdtemp()
        try:
            zipfile.ZipFile(io.BytesIO(download(pickle5_backport_url)), 'r').extractall(work_dir)
            subprocess.check_call([sys.executable, 'setup.py', 'bdist_wheel'], cwd=work_dir)
            for wheel in glob.glob(os.path.join(work_dir, 'dist', '*.whl')):
                zipfile.ZipFile(wheel, 'r').extractall(pickle5_dir)
        finally:
            shutil.rmtree(work_dir)
    bazel_env = dict(os.environ.copy(), **{'PYTHON%d_BIN_PATH' % sys.version_info[0]: sys.executable})
    bazel_build_cmd = ['bazel', 'build', '--verbose_failures']
    bazel_build_cmd.append('//:ray_pkg')
    if os.getenv('RAY_INSTALL_JAVA') == '1':
        # Also build binaries for Java if the above env variable exists.
        bazel_build_cmd.append('//java:all')
    subprocess.check_call(bazel_build_cmd, env=bazel_env)

class build_ext(_build_ext.build_ext):
    def run(self):
        if is_invalid_windows_platform():
            # https://github.com/msys2/MINGW-packages/blob/abd06ca92d876b9db05dd65f27d71c4ebe2673a9/mingw-w64-python2/0410-MINGW-build-extensions-with-GCC.patch#L53
            raise OSError("Please use official native CPython on Windows, not Cygwin/MSYS/MSYS2/MinGW/etc.")

        root_dir = os.path.dirname(os.getcwd())
        bazel_build(root_dir, self)

        # We also need to install pyarrow along with Ray, so make sure that the
        # relevant non-Python pyarrow files get copied.
        pyarrow_files = []
        for (root, dirs, filenames) in os.walk("./ray/pyarrow_files/pyarrow"):
            for name in filenames:
                pyarrow_files.append(os.path.join(root, name))

        # We also need to install pickle5 along with Ray, so make sure that the
        # relevant non-Python pickle5 files get copied.
        pickle5_files = []
        for (root, dirs, filenames) in os.walk("./ray/pickle5_files/pickle5"):
            for name in filenames:
                pickle5_files.append(os.path.join(root, name))

        files_to_include = ray_files + pyarrow_files + pickle5_files

        # Copy over the autogenerated protobuf Python bindings.
        for directory in generated_python_directories:
            for filename in os.listdir(directory):
                if filename[-3:] == ".py":
                    files_to_include.append(os.path.join(directory, filename))

        for filename in files_to_include:
            self.move_file(filename)

        # Try to copy over the optional files.
        for filename in optional_ray_files:
            try:
                self.move_file(filename)
            except Exception:
                print("Failed to copy optional file {}. This is ok."
                      .format(filename))

    def move_file(self, filename):
        # TODO(rkn): This feels very brittle. It may not handle all cases. See
        # https://github.com/apache/arrow/blob/master/python/setup.py for an
        # example.
        source = filename
        destination = os.path.join(self.build_lib, filename)
        # Create the target directory if it doesn't already exist.
        makedirs(os.path.dirname(destination), exist_ok=Trues)
        if not os.path.exists(destination):
            print("Copying {} to {}.".format(source, destination))
            shutil.copy(source, destination)


class BinaryDistribution(Distribution):
    def has_ext_modules(self):
        return True


def find_version(*filepath):
    # Extract version information from filepath
    here = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(here, *filepath)) as fp:
        version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                                  fp.read(), re.M)
        if version_match:
            return version_match.group(1)
        raise RuntimeError("Unable to find version string.")


requires = [
    "numpy >= 1.14",
    "filelock",
    "jsonschema",
    "funcsigs",
    "click",
    "colorama",
    "pytest",
    "pyyaml",
    "redis>=3.3.2",
    # NOTE: Don't upgrade the version of six! Doing so causes installation
    # problems. See https://github.com/ray-project/ray/issues/4169.
    "six >= 1.0.0",
    "faulthandler;python_version<'3.3'",
    "protobuf >= 3.8.0",
]

setup(
    name="ray",
    version=find_version("ray", "__init__.py"),
    author="Ray Team",
    author_email="ray-dev@googlegroups.com",
    description=("A system for parallel and distributed Python that unifies "
                 "the ML ecosystem."),
    long_description=open("../README.rst").read(),
    url="https://github.com/ray-project/ray",
    keywords=("ray distributed parallel machine-learning "
              "reinforcement-learning deep-learning python"),
    packages=find_packages(),
    cmdclass={"build_ext": build_ext},
    # The BinaryDistribution argument triggers build_ext.
    distclass=BinaryDistribution,
    install_requires=requires,
    setup_requires=["cython >= 0.29"],
    extras_require=extras,
    entry_points={
        "console_scripts": [
            "ray=ray.scripts.scripts:main",
            "rllib=ray.rllib.scripts:cli [rllib]", "tune=ray.tune.scripts:cli"
        ]
    },
    include_package_data=True,
    zip_safe=False,
    license="Apache 2.0")
