load("@rules_python//python:defs.bzl", "py_test")

test_srcs = glob(["**/*.py"])

py_test(
    name = "serve_failure_smoke_test",
    size = "medium",
    srcs = test_srcs,
    env = {
        "RAY_UNIT_TEST": "1",
    },
    main = "serve_failure.py",
    tags = [
        "exclusive",
        "team:serve",
    ],
    deps = [
        "//:ray_lib",
        "//python/ray/serve:serve_lib",
    ],
)

py_test(
    name = "single_deployment_1k_noop_replica_smoke_test",
    size = "medium",
    srcs = test_srcs,
    env = {
        "IS_SMOKE_TEST": "1",
    },
    main = "single_deployment_1k_noop_replica.py",
    tags = [
        "exclusive",
        "team:serve",
    ],
    deps = [
        "//:ray_lib",
        "//python/ray/serve:serve_lib",
    ],
)

py_test(
    name = "multi_deployment_1k_noop_replica_smoke_test",
    size = "medium",
    srcs = test_srcs,
    env = {
        "IS_SMOKE_TEST": "1",
    },
    main = "multi_deployment_1k_noop_replica.py",
    tags = [
        "exclusive",
        "team:serve",
    ],
    deps = [
        "//:ray_lib",
        "//python/ray/serve:serve_lib",
    ],
)

py_test(
    name = "autoscaling_single_deployment_smoke_test",
    size = "medium",
    srcs = test_srcs,
    env = {
        "IS_SMOKE_TEST": "1",
    },
    main = "autoscaling_single_deployment.py",
    tags = [
        "exclusive",
        "team:serve",
    ],
    deps = [
        "//:ray_lib",
        "//python/ray/serve:serve_lib",
    ],
)

py_test(
    name = "autoscaling_multi_deployment_smoke_test",
    size = "medium",
    srcs = test_srcs,
    env = {
        "IS_SMOKE_TEST": "1",
    },
    main = "autoscaling_multi_deployment.py",
    tags = [
        "exclusive",
        "team:serve",
    ],
    deps = [
        "//:ray_lib",
        "//python/ray/serve:serve_lib",
    ],
)

py_test(
    name = "test_alerts",
    size = "small",
    srcs = ["ray_release/tests/test_alerts.py"],
    tags = [
        "release_unit",
        "team:ci",
    ],
)

py_test(
    name = "test_buildkite",
    size = "small",
    srcs = ["ray_release/tests/test_buildkite.py"],
    tags = [
        "release_unit",
        "team:ci",
    ],
)

py_test(
    name = "test_cluster_manager",
    size = "small",
    srcs = ["ray_release/tests/test_cluster_manager.py"],
    tags = [
        "release_unit",
        "team:ci",
    ],
)

py_test(
    name = "test_config",
    size = "small",
    srcs = ["ray_release/tests/test_config.py"],
    tags = [
        "release_unit",
        "team:ci",
    ],
)

py_test(
    name = "test_glue",
    size = "small",
    srcs = ["ray_release/tests/test_glue.py"],
    tags = [
        "release_unit",
        "team:ci",
    ],
)

py_test(
    name = "test_run_script",
    size = "small",
    srcs = ["ray_release/tests/test_run_script.py"],
    tags = [
        "release_unit",
        "team:ci",
    ],
)

py_test(
    name = "test_wheels",
    size = "small",
    srcs = ["ray_release/tests/test_wheels.py"],
    tags = [
        "release_unit",
        "team:ci",
    ],
)
