# --------------------------------------------------------------------
# Tests from the python/ray/util/xgboost directory.
# Please keep these sorted alphabetically.
# --------------------------------------------------------------------
py_test(
    name = "simple_example",
    size = "small",
    srcs = ["simple_example.py"],
    tags = [
        "exclusive",
        "team:ml",
    ],
    deps = [":xgb_lib"],
)

py_test(
    name = "simple_tune",
    size = "small",
    srcs = ["simple_tune.py"],
    tags = [
        "exclusive",
        "team:ml",
    ],
    deps = [":xgb_lib"],
)

py_test(
    name = "test_client",
    size = "small",
    srcs = ["tests/test_client.py"],
    tags = [
        "client",
        "exclusive",
        "team:ml",
    ],
    deps = [":xgb_lib"],
)

# This is a dummy test dependency that causes the above tests to be
# re-run if any of these files changes.
py_library(
    name = "xgb_lib",
    srcs = glob(["**/*.py"]),
)
