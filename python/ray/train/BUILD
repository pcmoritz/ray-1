# --------------------------------------------------------------------
# Tests from the python/ray/train/examples directory.
# Please keep these sorted alphabetically.
# --------------------------------------------------------------------
py_test(
    name = "mlflow_fashion_mnist_example",
    size = "medium",
    srcs = ["examples/mlflow_fashion_mnist_example.py"],
    args = ["--smoke-test"],
    main = "examples/mlflow_fashion_mnist_example.py",
    tags = [
        "exclusive",
        "team:ml",
    ],
    deps = [":train_lib"],
)

py_test(
    name = "mlflow_simple_example",
    size = "medium",
    srcs = ["examples/mlflow_simple_example.py"],
    main = "examples/mlflow_simple_example.py",
    tags = [
        "exclusive",
        "team:ml",
    ],
    deps = [":train_lib"],
)

py_test(
    name = "tensorflow_quick_start",
    size = "medium",
    srcs = ["examples/tensorflow_quick_start.py"],
    main = "examples/tensorflow_quick_start.py",
    tags = [
        "exclusive",
        "team:ml",
    ],
    deps = [":train_lib"],
)

py_test(
    name = "torch_quick_start",
    size = "medium",
    srcs = ["examples/torch_quick_start.py"],
    main = "examples/torch_quick_start.py",
    tags = [
        "exclusive",
        "team:ml",
    ],
    deps = [":train_lib"],
)

py_test(
    name = "torch_tensorboard_profiler_example",
    size = "small",
    srcs = ["examples/torch_tensorboard_profiler_example.py"],
    main = "examples/torch_tensorboard_profiler_example.py",
    tags = [
        "exclusive",
        "team:ml",
    ],
    deps = [":train_lib"],
)

py_test(
    name = "transformers_example",
    size = "large",
    srcs = ["examples/transformers/transformers_example.py"],
    args = [
        "--model_name_or_path=bert-base-cased",
        "--task_name=mrpc",
        "--max_length=32",
        "--per_device_train_batch_size=64",
        "--max_train_steps=2",
        "--start_local",
        "--num_workers=2",
    ],
    main = "examples/transformers/transformers_example.py",
    tags = [
        "exclusive",
        "team:ml",
        "tune",
    ],
    deps = [":train_lib"],
)

py_test(
    name = "tune_cifar_pytorch_pbt_example",
    size = "medium",
    srcs = ["examples/tune_cifar_pytorch_pbt_example.py"],
    args = ["--smoke-test"],
    main = "examples/tune_cifar_pytorch_pbt_example.py",
    tags = [
        "exclusive",
        "pytorch",
        "team:ml",
        "tune",
    ],
    deps = [":train_lib"],
)

py_test(
    name = "tune_linear_dataset_example",
    size = "medium",
    srcs = ["examples/tune_linear_dataset_example.py"],
    args = [
        "--smoke-test",
        "--use-gpu",
    ],
    main = "examples/tune_linear_dataset_example.py",
    tags = [
        "exclusive",
        "gpu_only",
        "team:ml",
        "tune",
    ],
    deps = [":train_lib"],
)

py_test(
    name = "tune_linear_example",
    size = "medium",
    srcs = ["examples/tune_linear_example.py"],
    args = ["--smoke-test"],
    main = "examples/tune_linear_example.py",
    tags = [
        "exclusive",
        "team:ml",
        "tune",
    ],
    deps = [":train_lib"],
)

# --------------------------------------------------------------------
# Tests from the python/ray/train/tests directory.
# Please keep these sorted alphabetically.
# --------------------------------------------------------------------

py_test(
    name = "test_backend",
    size = "large",
    srcs = ["tests/test_backend.py"],
    tags = [
        "exclusive",
        "team:ml",
    ],
    deps = [":train_lib"],
)

py_test(
    name = "test_callbacks",
    size = "medium",
    srcs = ["tests/test_callbacks.py"],
    tags = [
        "exclusive",
        "team:ml",
    ],
    deps = [":train_lib"],
)

py_test(
    name = "test_examples",
    size = "large",
    srcs = ["tests/test_examples.py"],
    tags = [
        "exclusive",
        "team:ml",
    ],
    deps = [":train_lib"],
)

py_test(
    name = "test_gpu",
    size = "large",
    srcs = ["tests/test_gpu.py"],
    tags = [
        "exclusive",
        "gpu_only",
        "team:ml",
    ],
    deps = [":train_lib"],
)

py_test(
    name = "test_minimal",
    size = "small",
    srcs = ["tests/test_minimal.py"],
    tags = [
        "exclusive",
        "minimal",
        "team:ml",
    ],
    deps = [":train_lib"],
)

py_test(
    name = "test_session",
    size = "small",
    srcs = ["tests/test_session.py"],
    tags = [
        "exclusive",
        "team:ml",
    ],
    deps = [":train_lib"],
)

py_test(
    name = "test_results_preprocessors",
    size = "small",
    srcs = ["tests/test_results_preprocessors.py"],
    tags = [
        "exclusive",
        "team:ml",
    ],
    deps = [":train_lib"],
)

py_test(
    name = "test_trainer",
    size = "large",
    srcs = ["tests/test_trainer.py"],
    tags = [
        "exclusive",
        "team:ml",
    ],
    deps = [":train_lib"],
)

py_test(
    name = "test_tune",
    size = "medium",
    srcs = ["tests/test_tune.py"],
    tags = [
        "exclusive",
        "team:ml",
        "tune",
    ],
    deps = [":train_lib"],
)

py_test(
    name = "test_utils",
    size = "small",
    srcs = ["tests/test_utils.py"],
    tags = [
        "exclusive",
        "team:ml",
    ],
    deps = [":train_lib"],
)

py_test(
    name = "test_worker_group",
    size = "medium",
    srcs = ["tests/test_worker_group.py"],
    tags = [
        "exclusive",
        "team:ml",
    ],
    deps = [":train_lib"],
)

# This is a dummy test dependency that causes the above tests to be
# re-run if any of these files changes.
py_library(
    name = "train_lib",
    srcs = glob(
        ["**/*.py"],
        exclude = ["tests/*.py"],
    ),
)
