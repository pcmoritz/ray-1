workspace(name = "com_github_ray_project_ray")

load("@bazel_tools//tools/build_defs/repo:git.bzl", "git_repository", "new_git_repository")
load("//java:repo.bzl", "java_repositories")

java_repositories()

git_repository(
    name = "com_github_checkstyle_java",
    commit = "85f37871ca03b9d3fee63c69c8107f167e24e77b",
    remote = "https://github.com/ruifangChen/checkstyle_java",
)

git_repository(
    name = "com_github_nelhage_rules_boost",
    commit = "6d6fd834281cb8f8e758dd9ad76df86304bf1869",
    remote = "https://github.com/nelhage/rules_boost",
)

load("@com_github_nelhage_rules_boost//:boost/boost.bzl", "boost_deps")

boost_deps()

git_repository(
    name = "com_github_google_flatbuffers",
    commit = "63d51afd1196336a7d1f56a988091ef05deb1c62",
    remote = "https://github.com/google/flatbuffers.git",
)

git_repository(
    name = "com_google_googletest",
    commit = "3306848f697568aacf4bcca330f6bdd5ce671899",
    remote = "https://github.com/google/googletest",
)

git_repository(
    name = "com_github_gflags_gflags",
    remote = "https://github.com/gflags/gflags.git",
    tag = "v2.2.2",
)

new_git_repository(
    name = "com_github_google_glog",
    build_file = "@//bazel:BUILD.glog",
    commit = "5c576f78c49b28d89b23fbb1fc80f54c879ec02e",
    remote = "https://github.com/google/glog",
)

http_archive(
  name = "com_google_absl",
  urls = ["https://github.com/abseil/abseil-cpp/archive/7c7754fb3ed9ffb57d35fe8658f3ba4d73a31e72.zip"],  # 2019-03-14
  strip_prefix = "abseil-cpp-7c7754fb3ed9ffb57d35fe8658f3ba4d73a31e72",
  sha256 = "71d00d15fe6370220b6685552fb66e5814f4dd2e130f3836fc084c894943753f",
)

new_git_repository(
    name = "plasma",
    build_file = "@//bazel:BUILD.plasma",
    commit = "d00497b38be84fd77c40cbf77f3422f2a81c44f9",
    remote = "https://github.com/apache/arrow",
)

new_git_repository(
    name = "cython",
    build_file = "@//bazel:BUILD.cython",
    commit = "49414dbc7ddc2ca2979d6dbe1e44714b10d72e7e",
    remote = "https://github.com/cython/cython",
)

load("@//bazel:python_configure.bzl", "python_configure")

python_configure(name = "local_config_python")
