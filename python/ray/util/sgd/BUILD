# --------------------------------------------------------------------
# Tests from the python/ray/util/sgd/tests directory.
# Please keep these sorted alphabetically.
# --------------------------------------------------------------------
py_test(
    name = "test_client",
    size = "large",
    srcs = ["tests/test_client.py"],
    tags = [
        "client",
        "exclusive",
        "team:ml",
    ],
    deps = [":sgd_lib"],
)

py_test(
    name = "test_placement_groups",
    size = "medium",
    srcs = ["tests/test_placement_groups.py"],
    tags = [
        "exclusive",
        "team:ml",
    ],
    deps = [":sgd_lib"],
)

py_test(
    name = "test_tensorflow",
    size = "small",
    srcs = ["tests/test_tensorflow.py"],
    tags = [
        "exclusive",
        "team:ml",
        "tf",
    ],
    deps = [":sgd_lib"],
)

py_test(
    name = "test_tensorflow_client_mode",
    size = "small",
    srcs = ["tests/test_tensorflow.py"],
    main = "test_tensorflow.py",
    tags = [
        "client",
        "client_unit_tests",
        "exclusive",
        "team:ml",
        "tf",
    ],
)

py_test(
    name = "test_torch",
    size = "large",
    srcs = ["tests/test_torch.py"],
    tags = [
        "exclusive",
        "pytorch",
        "team:ml",
    ],
    deps = [":sgd_lib"],
)

py_test(
    name = "test_torch_2",
    size = "large",
    srcs = ["tests/test_torch_2.py"],
    tags = [
        "exclusive",
        "pytorch",
        "team:ml",
    ],
    deps = [":sgd_lib"],
)

py_test(
    name = "test_torch_3",
    size = "large",
    srcs = ["tests/test_torch_3.py"],
    tags = [
        "exclusive",
        "pytorch",
        "team:ml",
    ],
    deps = [":sgd_lib"],
)

py_test(
    name = "test_torch_basic",
    size = "small",
    srcs = ["tests/test_torch_basic.py"],
    tags = [
        "exclusive",
        "pytorch",
        "team:ml",
    ],
    deps = [":sgd_lib"],
)

py_test(
    name = "test_torch_basic_client_mode",
    size = "small",
    srcs = ["tests/test_torch_basic.py"],
    main = "test_torch_basic.py",
    tags = [
        "client",
        "client_unit_tests",
        "exclusive",
        "pytorch",
        "team:ml",
    ],
    deps = [":sgd_lib"],
)

py_test(
    name = "test_torch_failure",
    size = "large",
    srcs = ["tests/test_torch_failure.py"],
    tags = [
        "exclusive",
        "pytorch",
        "team:ml",
    ],
    deps = [":sgd_lib"],
)

py_test(
    name = "test_torch_runner",
    size = "small",
    srcs = ["tests/test_torch_runner.py"],
    tags = [
        "exclusive",
        "pytorch",
        "team:ml",
    ],
    deps = [":sgd_lib"],
)

# --------------------------------------------------------------------
# Tests from the python/ray/util/sgd/tf/examples directory.
# Please keep these sorted alphabetically.
# --------------------------------------------------------------------
py_test(
    name = "cifar_tf_example_1",
    size = "medium",
    srcs = ["tf/examples/cifar_tf_example.py"],
    args = [
        "--smoke-test",
        "--num-replicas=1",
    ],
    main = "tf/examples/cifar_tf_example.py",
    tags = [
        "exclusive",
        "team:ml",
        "tf",
    ],
    deps = [":sgd_lib"],
)

py_test(
    name = "cifar_tf_example_2",
    size = "medium",
    srcs = ["tf/examples/cifar_tf_example.py"],
    args = [
        "--smoke-test",
        "--num-replicas=2",
    ],
    main = "tf/examples/cifar_tf_example.py",
    tags = [
        "exclusive",
        "team:ml",
        "tf",
    ],
    deps = [":sgd_lib"],
)

py_test(
    name = "cifar_tf_example_2b",
    size = "small",
    srcs = ["tf/examples/cifar_tf_example.py"],
    args = [
        "--smoke-test",
        "--num-replicas=2",
        "--augment-data",
    ],
    main = "tf/examples/cifar_tf_example.py",
    tags = [
        "exclusive",
        "team:ml",
        "tf",
    ],
    deps = [":sgd_lib"],
)

py_test(
    name = "tensorflow_train_example_1",
    size = "small",
    srcs = ["tf/examples/tensorflow_train_example.py"],
    args = [
        "--num-replicas=1",
        "--smoke-test",
    ],
    main = "tf/examples/tensorflow_train_example.py",
    tags = [
        "exclusive",
        "team:ml",
        "tf",
    ],
    deps = [":sgd_lib"],
)

py_test(
    name = "tensorflow_train_example_2",
    size = "small",
    srcs = ["tf/examples/tensorflow_train_example.py"],
    args = [
        "--num-replicas=2",
        "--smoke-test",
    ],
    main = "tf/examples/tensorflow_train_example.py",
    tags = [
        "exclusive",
        "team:ml",
        "tf",
    ],
    deps = [":sgd_lib"],
)

py_test(
    name = "tensorflow_train_example_tune",
    size = "small",
    srcs = ["tf/examples/tensorflow_train_example.py"],
    args = [
        "--tune",
        "--smoke-test",
    ],
    main = "tf/examples/tensorflow_train_example.py",
    tags = [
        "exclusive",
        "team:ml",
        "tf",
    ],
    deps = [":sgd_lib"],
)

# --------------------------------------------------------------------
# Tests from the python/ray/util/sgd/torch/examples directory.
# Does not include subdirectories.
# Please keep these sorted alphabetically.
# --------------------------------------------------------------------
py_test(
    name = "cifar_pytorch_example_1",
    size = "medium",
    srcs = ["torch/examples/cifar_pytorch_example.py"],
    args = [
        "--smoke-test",
        "--num-workers=1",
    ],
    main = "torch/examples/cifar_pytorch_example.py",
    tags = [
        "exclusive",
        "pytorch",
        "team:ml",
    ],
    deps = [":sgd_lib"],
)

py_test(
    name = "cifar_pytorch_example_2",
    size = "medium",
    srcs = ["torch/examples/cifar_pytorch_example.py"],
    args = [
        "--smoke-test",
        "--num-workers=2",
    ],
    main = "torch/examples/cifar_pytorch_example.py",
    tags = [
        "exclusive",
        "pytorch",
        "team:ml",
    ],
    deps = [":sgd_lib"],
)

py_test(
    name = "cifar_pytorch_pbt",
    size = "medium",
    srcs = ["torch/examples/cifar_pytorch_pbt.py"],
    args = ["--smoke-test"],
    tags = [
        "exclusive",
        "pytorch",
        "team:ml",
    ],
    deps = [":sgd_lib"],
)

py_test(
    name = "dcgan",
    size = "small",
    srcs = ["torch/examples/dcgan.py"],
    args = [
        "--smoke-test",
        "--num-workers=2",
    ],
    tags = [
        "exclusive",
        "pytorch",
        "team:ml",
    ],
    deps = [":sgd_lib"],
)

py_test(
    name = "raysgd_torch_signatures",
    size = "small",
    srcs = ["torch/examples/raysgd_torch_signatures.py"],
    tags = [
        "exclusive",
        "pytorch",
        "team:ml",
    ],
    deps = [":sgd_lib"],
)

py_test(
    name = "train_example_1",
    size = "small",
    srcs = ["torch/examples/train_example.py"],
    args = [
        "--num-workers=1",
        "--smoke-test",
    ],
    main = "torch/examples/train_example.py",
    tags = [
        "exclusive",
        "pytorch",
        "team:ml",
    ],
    deps = [":sgd_lib"],
)

py_test(
    name = "train_example_2",
    size = "small",
    srcs = ["torch/examples/train_example.py"],
    args = [
        "--num-workers=2",
        "--smoke-test",
    ],
    main = "torch/examples/train_example.py",
    tags = [
        "exclusive",
        "pytorch",
        "team:ml",
    ],
    deps = [":sgd_lib"],
)

py_test(
    name = "tune_example_1",
    size = "small",
    srcs = ["torch/examples/tune_example.py"],
    args = [
        "--num-workers=1",
        "--smoke-test",
    ],
    main = "torch/examples/tune_example.py",
    tags = [
        "exclusive",
        "pytorch",
        "team:ml",
    ],
    deps = [":sgd_lib"],
)

py_test(
    name = "tune_example_2",
    size = "small",
    srcs = ["torch/examples/tune_example.py"],
    args = [
        "--num-workers=2",
        "--smoke-test",
    ],
    main = "torch/examples/tune_example.py",
    tags = [
        "exclusive",
        "pytorch",
        "team:ml",
    ],
    deps = [":sgd_lib"],
)

py_test(
    name = "tune_example_3",
    size = "small",
    srcs = ["torch/examples/tune_example.py"],
    args = [
        "--num-workers=2",
        "--smoke-test",
        "--lr-reduce-on-plateau",
    ],
    main = "torch/examples/tune_example.py",
    tags = [
        "exclusive",
        "pytorch",
        "team:ml",
    ],
    deps = [":sgd_lib"],
)

# --------------------------------------------------------------------
# Tests from the python/ray/util/sgd/torch/examples/* directories.
# Only covers subdirectories.
# Please keep these sorted alphabetically.
# --------------------------------------------------------------------
py_test(
    name = "benchmark",
    size = "small",
    srcs = ["torch/examples/benchmarks/benchmark.py"],
    args = ["--smoke-test"],
    tags = [
        "exclusive",
        "pytorch",
        "team:ml",
    ],
    deps = [":sgd_lib"],
)

py_test(
    name = "image_models",
    size = "small",
    srcs = ["torch/examples/image_models/train.py"],
    args = [
        "--no-gpu",
        "--mock-data",
        "--smoke-test",
        "--ray-num-workers=2",
        "--model=mobilenetv3_small_075",
        "data",
    ],
    main = "torch/examples/image_models/train.py",
    tags = [
        "exclusive",
        "pytorch",
        "team:ml",
    ],
    deps = [":sgd_lib"],
)

# --------------------------------------------------------------------
# SGD related tests from the ../../../../release directory.
# Please keep these sorted alphabetically.
# --------------------------------------------------------------------

py_test(
    name = "pytorch_pbt_failure",
    size = "medium",
    srcs = ["torch/examples/pytorch_pbt_failure.py"],
    args = ["--smoke-test"],
    tags = [
        "exlusive",
        "pytorch",
        "release",
        "team:ml",
    ],
    deps = [":sgd_lib"],
)

# This is a dummy test dependency that causes the above tests to be
# re-run if any of these files changes.
py_library(
    name = "sgd_lib",
    srcs = glob(
        ["**/*.py"],
        exclude = [
            "tests/*.py",
            "v2/*",
        ],
    ),
)
