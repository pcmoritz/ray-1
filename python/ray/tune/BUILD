load("//bazel:python.bzl", "py_test_module_list")

# --------------------------------------------------------------------
# Tests from the python/ray/tune/tests directory.
# Covers all tests starting with `test_`.
# Please keep these sorted alphabetically.
#
# Tags:
# "team:ml": Tag indicating this test is owned by the ML team.
# "client": Test uses the ray client.
# "example": Test runs a tune example script.
# "exclusive": ???
# "py37": Test requires py3.7 or later.
# "soft_imports": Tests checking whether Tune runs without any of its soft dependencies.
# "pytorch": Test uses PyTorch.
# "tensorflow": Test uses TensorFlow.
# "tests_dir_A-Z": Tags to spread out tests. Make sure you tag your newly added tests with this.
# --------------------------------------------------------------------
py_test(
    name = "test_actor_reuse",
    size = "medium",
    srcs = ["tests/test_actor_reuse.py"],
    tags = [
        "exclusive",
        "team:ml",
        "tests_dir_A",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "test_api",
    size = "large",
    srcs = ["tests/test_api.py"],
    tags = [
        "exclusive",
        "rllib",
        "team:ml",
        "tests_dir_A",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "test_automl_searcher",
    size = "small",
    srcs = ["tests/test_automl_searcher.py"],
    tags = [
        "exclusive",
        "team:ml",
        "tests_dir_A",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "test_checkpoint_manager",
    size = "small",
    srcs = ["tests/test_checkpoint_manager.py"],
    tags = [
        "exclusive",
        "team:ml",
        "tests_dir_C",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "test_client",
    size = "large",
    srcs = ["tests/test_client.py"],
    tags = [
        "client",
        "exclusive",
        "py37",
        "team:ml",
        "tests_dir_C",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "test_cloud",
    size = "medium",
    srcs = ["tests/test_cloud.py"],
    tags = [
        "exclusive",
        "team:ml",
        "tests_dir_C",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "test_cluster",
    size = "large",
    srcs = ["tests/test_cluster.py"],
    tags = [
        "exclusive",
        "rllib",
        "team:ml",
        "tests_dir_C",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "test_cluster_searcher",
    size = "large",
    srcs = ["tests/test_cluster_searcher.py"],
    tags = [
        "exclusive",
        "team:ml",
        "tests_dir_C",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "test_commands",
    size = "medium",
    srcs = ["tests/test_commands.py"],
    tags = [
        "exclusive",
        "team:ml",
        "tests_dir_C",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "test_convergence",
    size = "medium",
    srcs = ["tests/test_convergence.py"],
    tags = [
        "exclusive",
        "team:ml",
        "tests_dir_C",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "test_dependency",
    size = "small",
    srcs = ["tests/test_dependency.py"],
    tags = [
        "exclusive",
        "team:ml",
        "tests_dir_D",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "test_experiment",
    size = "small",
    srcs = ["tests/test_experiment.py"],
    tags = [
        "exclusive",
        "team:ml",
        "tests_dir_E",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "test_experiment_analysis",
    size = "medium",
    srcs = ["tests/test_experiment_analysis.py"],
    tags = [
        "exclusive",
        "team:ml",
        "tests_dir_E",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "test_experiment_analysis_mem",
    size = "medium",
    srcs = ["tests/test_experiment_analysis_mem.py"],
    tags = [
        "exclusive",
        "team:ml",
        "tests_dir_E",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "test_function_api",
    size = "medium",
    srcs = ["tests/test_function_api.py"],
    tags = [
        "exclusive",
        "team:ml",
        "tests_dir_F",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "test_integration_comet",
    size = "small",
    srcs = ["tests/test_integration_comet.py"],
    tags = [
        "exclusive",
        "team:ml",
        "tests_dir_I",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "test_integration_docker",
    size = "small",
    srcs = ["tests/test_integration_docker.py"],
    tags = [
        "exclusive",
        "team:ml",
        "tests_dir_I",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "test_integration_kubernetes",
    size = "small",
    srcs = ["tests/test_integration_kubernetes.py"],
    tags = [
        "exclusive",
        "team:ml",
        "tests_dir_I",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "test_integration_pytorch_lightning",
    size = "small",
    srcs = ["tests/test_integration_pytorch_lightning.py"],
    tags = [
        "exclusive",
        "team:ml",
        "tests_dir_I",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "test_integration_wandb",
    size = "small",
    srcs = ["tests/test_integration_wandb.py"],
    tags = [
        "exclusive",
        "team:ml",
        "tests_dir_I",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "test_integration_mlflow",
    size = "small",
    srcs = ["tests/test_integration_mlflow.py"],
    tags = [
        "exclusive",
        "team:ml",
        "tests_dir_I",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "test_logger",
    size = "small",
    srcs = ["tests/test_logger.py"],
    tags = [
        "team:ml",
        "tests_dir_L",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "test_multinode_sync",
    size = "large",
    srcs = ["tests/test_multinode_sync.py"],
    tags = [
        "multinode",
        "team:ml",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "test_progress_reporter",
    size = "medium",
    srcs = ["tests/test_progress_reporter.py"],
    tags = [
        "exclusive",
        "team:ml",
        "tests_dir_P",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "test_resource_updater",
    size = "large",
    srcs = ["tests/test_resource_updater.py"],
    tags = [
        "exclusive",
        "team:ml",
        "tests_dir_R",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "test_ray_trial_executor",
    size = "large",
    srcs = ["tests/test_ray_trial_executor.py"],
    tags = [
        "exclusive",
        "team:ml",
        "tests_dir_R",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "test_run_experiment",
    size = "medium",
    srcs = ["tests/test_run_experiment.py"],
    tags = [
        "exclusive",
        "team:ml",
        "tests_dir_R",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "test_remote",
    size = "medium",
    srcs = ["tests/test_remote.py"],
    tags = [
        "exclusive",
        "team:ml",
        "tests_dir_R",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "test_result_grid",
    size = "small",
    srcs = ["tests/test_result_grid.py"],
    tags = [
        "exclusive",
        "team:ml",
        "tests_dir_R",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "test_sample",
    size = "large",
    srcs = ["tests/test_sample.py"],
    tags = [
        "exclusive",
        "team:ml",
        "tests_dir_S",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "test_searchers",
    size = "medium",
    srcs = ["tests/test_searchers.py"],
    tags = [
        "exclusive",
        "team:ml",
        "tests_dir_S",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "test_soft_imports",
    size = "small",
    srcs = ["tests/test_soft_imports.py"],
    tags = [
        "soft_imports",
        "team:ml",
        "tests_dir_S",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "test_sync",
    size = "medium",
    srcs = ["tests/test_sync.py"],
    tags = [
        "exclusive",
        "team:ml",
        "tests_dir_S",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "test_trainable_util",
    size = "small",
    srcs = ["tests/test_trainable_util.py"],
    tags = [
        "exclusive",
        "team:ml",
        "tests_dir_T",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "test_trial_runner",
    size = "medium",
    srcs = ["tests/test_trial_runner.py"],
    tags = [
        "exclusive",
        "team:ml",
        "tests_dir_T",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "test_trial_runner_2",
    size = "medium",
    srcs = ["tests/test_trial_runner_2.py"],
    tags = [
        "exclusive",
        "team:ml",
        "tests_dir_T",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "test_trial_runner_3",
    size = "medium",
    srcs = ["tests/test_trial_runner_3.py"],
    tags = [
        "exclusive",
        "team:ml",
        "tests_dir_T",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "test_trial_runner_pg",
    size = "medium",
    srcs = ["tests/test_trial_runner_pg.py"],
    tags = [
        "exclusive",
        "team:ml",
        "tests_dir_T",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "test_trial_runner_callbacks",
    size = "small",
    srcs = ["tests/test_trial_runner_callbacks.py"],
    tags = [
        "exclusive",
        "team:ml",
        "tests_dir_T",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "test_var",
    size = "medium",
    srcs = ["tests/test_var.py"],
    tags = [
        "exclusive",
        "team:ml",
        "tests_dir_V",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "test_trial_scheduler",
    size = "large",
    srcs = ["tests/test_trial_scheduler.py"],
    tags = [
        "exclusive",
        "team:ml",
        "tests_dir_T",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "test_trial_scheduler_pbt",
    size = "large",
    srcs = ["tests/test_trial_scheduler_pbt.py"],
    tags = [
        "exclusive",
        "team:ml",
        "tests_dir_T",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "test_trial_scheduler_resource_changing",
    size = "small",
    srcs = ["tests/test_trial_scheduler_resource_changing.py"],
    tags = [
        "exclusive",
        "team:ml",
        "tests_dir_T",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "test_tune_restore_warm_start",
    size = "large",
    srcs = ["tests/test_tune_restore_warm_start.py"],
    tags = [
        "exclusive",
        "team:ml",
        "tests_dir_T",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "test_tune_restore",
    size = "large",
    srcs = ["tests/test_tune_restore.py"],
    tags = [
        "exclusive",
        "rllib",
        "team:ml",
        "tests_dir_T",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "test_tune_save_restore",
    size = "small",
    srcs = ["tests/test_tune_save_restore.py"],
    tags = [
        "exclusive",
        "team:ml",
        "tests_dir_T",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "test_tune_server",
    size = "medium",
    srcs = ["tests/test_tune_server.py"],
    tags = [
        "exclusive",
        "team:ml",
        "tests_dir_T",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "test_tuner",
    size = "medium",
    srcs = ["tests/test_tuner.py"],
    tags = [
        "exclusive",
        "team:ml",
        "tests_dir_T",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "test_utils",
    size = "small",
    srcs = ["tests/test_utils.py"],
    tags = [
        "exclusive",
        "team:ml",
        "tests_dir_U",
    ],
    deps = [":tune_lib"],
)

py_test_module_list(
    size = "large",
    extra_srcs = [],
    files = [
        "tests/test_trial_executor_inheritance.py",
    ],
    tags = [
        "exclusive",
        "manual",
        "team:ml",
    ],
    deps = ["//:tune_lib"],
)

# --------------------------------------------------------------------
# Tests from the python/ray/tune/tests directory.
# Covers all remaining tests that do not start with `test_`.
# Please keep these sorted alphabetically.
# --------------------------------------------------------------------
py_test(
    name = "example",
    size = "small",
    srcs = ["tests/example.py"],
    tags = [
        "example",
        "exclusive",
        "team:ml",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "ext_pytorch",
    size = "large",
    srcs = ["tests/ext_pytorch.py"],
    tags = [
        "example",
        "exclusive",
        "team:ml",
    ],
    deps = [":tune_lib"],
)

# Todo: Ensure MPLBACKEND=Agg
py_test(
    name = "tutorial",
    size = "medium",
    srcs = ["tests/tutorial.py"],
    tags = [
        "example",
        "exclusive",
        "team:ml",
    ],
    deps = [":tune_lib"],
)

# --------------------------------------------------------------------
# Examples from the python/ray/tune/examples directory.
# Please keep these sorted alphabetically.
# --------------------------------------------------------------------
py_test(
    name = "async_hyperband_example",
    size = "small",
    srcs = ["examples/async_hyperband_example.py"],
    args = ["--smoke-test"],
    tags = [
        "example",
        "exclusive",
        "team:ml",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "ax_example",
    size = "medium",
    srcs = ["examples/ax_example.py"],
    args = ["--smoke-test"],
    tags = [
        "example",
        "exclusive",
        "py37",
        "team:ml",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "bayesopt_example",
    size = "medium",
    srcs = ["examples/bayesopt_example.py"],
    args = ["--smoke-test"],
    tags = [
        "example",
        "exclusive",
        "team:ml",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "blendsearch_example",
    size = "medium",
    srcs = ["examples/blendsearch_example.py"],
    args = ["--smoke-test"],
    tags = [
        "example",
        "exclusive",
        "team:ml",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "bohb_example",
    size = "medium",
    srcs = ["examples/bohb_example.py"],
    tags = [
        "example",
        "exclusive",
        "team:ml",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "cfo_example",
    size = "small",
    srcs = ["examples/cfo_example.py"],
    args = ["--smoke-test"],
    tags = [
        "example",
        "exclusive",
        "team:ml",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "cifar10_pytorch",
    size = "medium",
    srcs = ["examples/cifar10_pytorch.py"],
    args = ["--smoke-test"],
    tags = [
        "example",
        "exclusive",
        "pytorch",
        "team:ml",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "custom_func_checkpointing",
    size = "small",
    srcs = ["examples/custom_func_checkpointing.py"],
    args = ["--smoke-test"],
    tags = [
        "example",
        "exclusive",
        "team:ml",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "test_torch_trainable",
    size = "medium",
    srcs = ["tests/test_torch_trainable.py"],
    tags = [
        "example",
        "exclusive",
        "pytorch",
        "team:ml",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "test_tensorflow_trainable",
    size = "medium",
    srcs = ["tests/test_tensorflow_trainable.py"],
    tags = [
        "example",
        "exclusive",
        "team:ml",
        "tensorflow",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "test_horovod",
    size = "medium",
    srcs = ["tests/test_horovod.py"],
    tags = [
        "example",
        "exclusive",
        "py37",
        "team:ml",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "ddp_mnist_torch",
    size = "small",
    srcs = ["examples/ddp_mnist_torch.py"],
    args = ["--num-workers=2"],
    tags = [
        "example",
        "exclusive",
        "pytorch",
        "team:ml",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "tf_distributed_keras_example",
    size = "small",
    srcs = ["examples/tf_distributed_keras_example.py"],
    args = ["--smoke-test"],
    tags = [
        "example",
        "exclusive",
        "team:ml",
        "tensorflow",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "dragonfly_example",
    size = "medium",
    srcs = ["examples/dragonfly_example.py"],
    args = ["--smoke-test"],
    tags = [
        "example",
        "exclusive",
        "team:ml",
    ],
    deps = [":tune_lib"],
)

# Does not work without awscli tool installed. Check if can be mocked.
# py_test(
#     name = "durable_trainable_example",
#     size = "medium",
#     srcs = ["examples/durable_trainable_example.py"],
#     deps = [":tune_lib"],
#     tags = ["team:ml", "exclusive", "example"],
#     args = ["--local", "--mock-storage"]
# )

py_test(
    name = "genetic_example",
    size = "small",
    srcs = ["examples/genetic_example.py"],
    args = ["--smoke-test"],
    tags = [
        "example",
        "exclusive",
        "team:ml",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "hebo_example",
    size = "medium",
    srcs = ["examples/hebo_example.py"],
    args = ["--smoke-test"],
    tags = [
        "example",
        "exclusive",
        "team:ml",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "horovod_simple",
    size = "medium",
    srcs = ["examples/horovod_simple.py"],
    args = ["--smoke-test"],
    tags = [
        "example",
        "exclusive",
        "py37",
        "team:ml",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "hyperband_example",
    size = "medium",
    srcs = ["examples/hyperband_example.py"],
    args = ["--smoke-test"],
    tags = [
        "example",
        "exclusive",
        "team:ml",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "hyperband_function_example",
    size = "small",
    srcs = ["examples/hyperband_function_example.py"],
    args = ["--smoke-test"],
    tags = [
        "example",
        "exclusive",
        "team:ml",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "hyperopt_conditional_search_space_example",
    size = "medium",
    srcs = ["examples/hyperopt_conditional_search_space_example.py"],
    args = ["--smoke-test"],
    tags = [
        "example",
        "exclusive",
        "team:ml",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "lightgbm_example",
    size = "small",
    srcs = ["examples/lightgbm_example.py"],
    tags = [
        "example",
        "exclusive",
        "team:ml",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "lightgbm_example_cv",
    size = "small",
    srcs = ["examples/lightgbm_example.py"],
    args = ["--use-cv"],
    main = "examples/lightgbm_example.py",
    tags = [
        "example",
        "exclusive",
        "team:ml",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "logging_example",
    size = "small",
    srcs = ["examples/logging_example.py"],
    args = ["--smoke-test"],
    tags = [
        "example",
        "exclusive",
        "team:ml",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "mlflow_example",
    size = "medium",
    srcs = ["examples/mlflow_example.py"],
    tags = [
        "example",
        "exclusive",
        "team:ml",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "mlflow_ptl",
    size = "medium",
    srcs = ["examples/mlflow_ptl.py"],
    args = ["--smoke-test"],
    tags = [
        "example",
        "exclusive",
        "py37",
        "pytorch",
        "team:ml",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "mnist_pytorch",
    size = "small",
    srcs = ["examples/mnist_pytorch.py"],
    args = ["--smoke-test"],
    tags = [
        "example",
        "exclusive",
        "pytorch",
        "team:ml",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "mnist_pytorch_lightning",
    size = "medium",
    srcs = ["examples/mnist_pytorch_lightning.py"],
    args = ["--smoke-test"],
    tags = [
        "example",
        "exclusive",
        "pytorch",
        "team:ml",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "mnist_ptl_mini",
    size = "large",
    srcs = ["examples/mnist_ptl_mini.py"],
    args = ["--smoke-test"],
    tags = [
        "example",
        "exclusive",
        "pytorch",
        "team:ml",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "mnist_pytorch_trainable",
    size = "small",
    srcs = ["examples/mnist_pytorch_trainable.py"],
    args = ["--smoke-test"],
    tags = [
        "example",
        "exclusive",
        "pytorch",
        "team:ml",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "mxnet_example",
    size = "small",
    srcs = ["examples/mxnet_example.py"],
    args = ["--smoke-test"],
    tags = [
        "example",
        "exclusive",
        "team:ml",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "nevergrad_example",
    size = "small",
    srcs = ["examples/nevergrad_example.py"],
    args = ["--smoke-test"],
    tags = [
        "example",
        "exclusive",
        "team:ml",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "optuna_define_by_run_example",
    size = "small",
    srcs = ["examples/optuna_define_by_run_example.py"],
    args = ["--smoke-test"],
    tags = [
        "example",
        "exclusive",
        "team:ml",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "optuna_example",
    size = "small",
    srcs = ["examples/optuna_example.py"],
    args = ["--smoke-test"],
    tags = [
        "example",
        "exclusive",
        "team:ml",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "optuna_multiobjective_example",
    size = "small",
    srcs = ["examples/optuna_multiobjective_example.py"],
    args = ["--smoke-test"],
    tags = [
        "example",
        "exclusive",
        "team:ml",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "pb2_example",
    size = "medium",
    srcs = ["examples/pb2_example.py"],
    args = ["--smoke-test"],
    tags = [
        "example",
        "exclusive",
        "team:ml",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "pbt_convnet_example",
    size = "small",
    srcs = ["examples/pbt_convnet_example.py"],
    args = ["--smoke-test"],
    tags = [
        "example",
        "exclusive",
        "team:ml",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "pbt_convnet_function_example",
    size = "small",
    srcs = ["examples/pbt_convnet_function_example.py"],
    args = ["--smoke-test"],
    tags = [
        "example",
        "exclusive",
        "team:ml",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "pbt_dcgan_mnist_func",
    size = "medium",
    srcs = ["examples/pbt_dcgan_mnist/pbt_dcgan_mnist_func.py"],
    args = ["--smoke-test"],
    tags = [
        "example",
        "exclusive",
        "team:ml",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "pbt_dcgan_mnist_trainable",
    size = "medium",
    srcs = ["examples/pbt_dcgan_mnist/pbt_dcgan_mnist_trainable.py"],
    args = ["--smoke-test"],
    tags = [
        "example",
        "exclusive",
        "team:ml",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "pbt_example",
    size = "small",
    srcs = ["examples/pbt_example.py"],
    args = ["--smoke-test"],
    tags = [
        "example",
        "exclusive",
        "team:ml",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "pbt_function",
    size = "medium",
    srcs = ["examples/pbt_function.py"],
    args = ["--smoke-test"],
    tags = [
        "example",
        "exclusive",
        "team:ml",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "pbt_memnn_example",
    size = "medium",
    srcs = ["examples/pbt_memnn_example.py"],
    args = ["--smoke-test"],
    tags = [
        "example",
        "exclusive",
        "team:ml",
    ],
    deps = [":tune_lib"],
)

# Requires GPUs. Add smoke test?
# py_test(
#     name = "pbt_ppo_example",
#     size = "medium",
#     srcs = ["examples/pbt_ppo_example.py"],
#     deps = [":tune_lib"],
#     tags = ["team:ml", "exclusive", "example"],
#     args = ["--smoke-test"]
# )

py_test(
    name = "pbt_transformers",
    size = "large",
    srcs = ["examples/pbt_transformers/pbt_transformers.py"],
    args = ["--smoke-test"],
    tags = [
        "example",
        "exclusive",
        "team:ml",
    ],
    deps = [":tune_lib"],
)

# Requires GPUs. Add smoke test?
# py_test(
#     name = "pbt_tune_cifar10_with_keras",
#     size = "medium",
#     srcs = ["examples/pbt_tune_cifar10_with_keras.py"],
#     deps = [":tune_lib"],
#     tags = ["team:ml", "exclusive", "example"],
#     args = ["--smoke-test"]
# )

# Needs SigOpt API key.
py_test(
    name = "sigopt_example",
    size = "medium",
    srcs = ["examples/sigopt_example.py"],
    args = ["--smoke-test"],
    tags = [
        "example",
        "exclusive",
        "team:ml",
    ],
    deps = [":tune_lib"],
)

# Needs SigOpt API key.
py_test(
    name = "sigopt_multi_objective_example",
    size = "medium",
    srcs = ["examples/sigopt_multi_objective_example.py"],
    args = ["--smoke-test"],
    tags = [
        "example",
        "exclusive",
        "team:ml",
    ],
    deps = [":tune_lib"],
)

# Needs SigOpt API key.
py_test(
    name = "sigopt_prior_beliefs_example",
    size = "medium",
    srcs = ["examples/sigopt_prior_beliefs_example.py"],
    args = ["--smoke-test"],
    tags = [
        "example",
        "exclusive",
        "team:ml",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "skopt_example",
    size = "medium",
    srcs = ["examples/skopt_example.py"],
    args = ["--smoke-test"],
    tags = [
        "example",
        "exclusive",
        "team:ml",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "tf_mnist_example",
    size = "medium",
    srcs = ["examples/tf_mnist_example.py"],
    args = ["--smoke-test"],
    tags = [
        "example",
        "exclusive",
        "team:ml",
        "tf",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "tune_basic_example",
    size = "small",
    srcs = ["examples/tune_basic_example.py"],
    args = ["--smoke-test"],
    tags = [
        "example",
        "exclusive",
        "team:ml",
    ],
    deps = [":tune_lib"],
)

# Downloads too much data.
# py_test(
#     name = "tune_cifar10_gluon",
#     size = "medium",
#     srcs = ["examples/tune_cifar10_gluon.py"],
#     deps = [":tune_lib"],
#     tags = ["team:ml", "exclusive", "example"],
#     args = ["--model SqueezeNet1.0", "--smoke-test"]
# )

py_test(
    name = "tune_mnist_keras",
    size = "medium",
    srcs = ["examples/tune_mnist_keras.py"],
    args = ["--smoke-test"],
    tags = [
        "example",
        "exclusive",
        "team:ml",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "wandb_example",
    size = "small",
    srcs = ["examples/wandb_example.py"],
    args = ["--mock-api"],
    tags = [
        "example",
        "exclusive",
        "team:ml",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "xgboost_example",
    size = "small",
    srcs = ["examples/xgboost_example.py"],
    tags = [
        "example",
        "exclusive",
        "team:ml",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "xgboost_example_cv",
    size = "small",
    srcs = ["examples/xgboost_example.py"],
    args = ["--use-cv"],
    main = "examples/xgboost_example.py",
    tags = [
        "example",
        "exclusive",
        "team:ml",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "xgboost_dynamic_resources_example",
    size = "large",
    srcs = ["examples/xgboost_dynamic_resources_example.py"],
    args = ["--test"],
    tags = [
        "example",
        "exclusive",
        "team:ml",
    ],
    deps = [":tune_lib"],
)

py_test(
    name = "zoopt_example",
    size = "small",
    srcs = ["examples/zoopt_example.py"],
    args = ["--smoke-test"],
    tags = [
        "example",
        "exclusive",
        "team:ml",
    ],
    deps = [":tune_lib"],
)

# --------------------------------------------------------------------
# Tune related tests from the ../../../../release directory.
# Please keep these sorted alphabetically.
# --------------------------------------------------------------------

py_test(
    name = "horovod_cifar_pbt_example",
    size = "medium",
    srcs = ["examples/horovod_cifar_pbt_example.py"],
    args = ["--smoke-test"],
    tags = [
        "example",
        "exlusive",
        "py37",
        "pytorch",
        "release",
        "team:ml",
    ],
    deps = [":tune_lib"],
)

# This is a dummy test dependency that causes the above tests to be
# re-run if any of these files changes.
py_library(
    name = "tune_lib",
    srcs = glob(
        ["**/*.py"],
        exclude = ["tests/*.py"],
    ),
)
