# --------------------------------------------------------------------
# Tests from the python/ray.workflow/tests directory.
# Covers all tests starting with `test_`.
# Please keep these sorted alphabetically.
# --------------------------------------------------------------------
load("//bazel:python.bzl", "py_test_module_list")

SRCS = [] + select({
    "@bazel_tools//src/conditions:windows": glob([
        # TODO(mehrdadn): This should be added for all platforms once resulting errors are fixed
        "**/conftest.py",
    ]),
    "//conditions:default": [],
})

LARGE_TESTS = [
    "tests/test_recovery.py",
    "tests/test_basic_workflows_2.py",
    "tests/test_metadata.py",
]

py_test_module_list(
    size = "medium",
    extra_srcs = SRCS,
    files = glob(
        [
            "tests/test_*.py",
            "examples/**/*.py",
        ],
        exclude = LARGE_TESTS,
    ),
    tags = [
        "exclusive",
        "team:core",
    ],
    deps = ["//:ray_lib"],
)

py_test_module_list(
    size = "large",
    extra_srcs = SRCS,
    files = LARGE_TESTS,
    tags = [
        "exclusive",
        "team:core",
    ],
    deps = ["//:ray_lib"],
)
