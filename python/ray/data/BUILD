# --------------------------------------------------------------------
# Tests from the python/ray/data/tests directory.
# Covers all tests starting with `test_`.
# Please keep these sorted alphabetically.
# --------------------------------------------------------------------
load("//bazel:python.bzl", "py_test_module_list")

SRCS = [] + select({
    "@bazel_tools//src/conditions:windows": glob([
        "**/conftest.py",
    ]),
    "//conditions:default": [],
})

py_test_module_list(
    size = "large",
    extra_srcs = SRCS,
    files = glob(["tests/test_*.py"]),
    tags = [
        "exclusive",
        "team:core",
    ],
    deps = ["//:ray_lib"],
)
