# --------------------------------------------------------------------
# BAZEL/Buildkite-CI test cases.
# --------------------------------------------------------------------

# To add new RLlib tests, first find the correct category of your new test
# within this file.

# All new tests - within their category - should be added alphabetically!
# Do not just add tests to the bottom of the file.

# Currently we have the following categories:

# - Learning tests/regression, tagged:
# -- "learning_tests_[discrete|continuous]": distinguish discrete
#    actions vs continuous actions.
# -- "fake_gpus": Tests that run using 2 fake GPUs.

# - Quick agent compilation/tune-train tests, tagged "quick_train".
#   NOTE: These should be obsoleted in favor of "trainers_dir" tests as
#         they cover the same functionaliy.

# - Folder-bound tests, tagged with the name of the top-level dir:
#   - `env` directory tests.
#   - `evaluation` directory tests.
#   - `execution` directory tests.
#   - `models` directory tests.
#   - `policy` directory tests.
#   - `utils` directory tests.

# - Trainer ("agents") tests, tagged "trainers_dir".

# - Tests directory (everything in rllib/tests/...), tagged: "tests_dir" and
#   "tests_dir_[A-Z]"

# - Examples directory (everything in rllib/examples/...), tagged: "examples" and
#   "examples_[A-Z]"

# - Memory leak tests tagged "memory_leak_tests".

# Note: The "examples" and "tests_dir" tags have further sub-tags going by the
# starting letter of the test name (e.g. "examples_A", or "tests_dir_F") for
# split-up purposes in buildkite.

# Note: There is a special directory in examples: "documentation" which contains
# all code that is linked to from within the RLlib docs. This code is tested
# separately via the "documentation" tag.

# Additional tags are:
# - "team:ml": Indicating that all tests in this file are the responsibility of
#   the ML Team.
# - "needs_gpu": Indicating that a test needs to have a GPU in order to run.
# - "gpu": Indicating that a test may (but doesn't have to) be run in the GPU
#   pipeline, defined in .buildkite/pipeline.gpu.yaml.
# - "multi-gpu": Indicating that a test will definitely be run in the Large GPU
#   pipeline, defined in .buildkite/pipeline.gpu.large.yaml.
# - "no_gpu": Indicating that a test should not be run in the GPU pipeline due
#   to certain incompatibilities.
# - "no_tf_eager_tracing": Exclude this test from tf-eager tracing tests.
# - "torch_only": Only run this test case with framework=torch.

# Our .buildkite/pipeline.yml and .buildkite/pipeline.gpu.yml files execute all
# these tests in n different jobs.

load("//bazel:python.bzl", "py_test_module_list")

# --------------------------------------------------------------------
# Agents learning regression tests.
#
# Tag: learning_tests
#
# This will test all yaml files (via `rllib train`)
# inside rllib/tuned_examples/[algo-name] for actual learning success.
# --------------------------------------------------------------------

# A2C/A3C
py_test(
    name = "learning_tests_cartpole_a2c",
    size = "large",
    srcs = ["tests/run_regression_tests.py"],
    args = ["--yaml-dir=tuned_examples/a3c"],
    data = ["tuned_examples/a3c/cartpole-a2c.yaml"],
    main = "tests/run_regression_tests.py",
    tags = [
        "learning_tests",
        "learning_tests_cartpole",
        "learning_tests_discrete",
        "team:ml",
    ],
)

py_test(
    name = "learning_tests_cartpole_a2c_fake_gpus",
    size = "large",
    srcs = ["tests/run_regression_tests.py"],
    args = ["--yaml-dir=tuned_examples/a3c"],
    data = ["tuned_examples/a3c/cartpole-a2c-fake-gpus.yaml"],
    main = "tests/run_regression_tests.py",
    tags = [
        "fake_gpus",
        "learning_tests",
        "learning_tests_cartpole",
        "learning_tests_discrete",
        "team:ml",
    ],
)

py_test(
    name = "learning_tests_cartpole_a3c",
    size = "large",
    srcs = ["tests/run_regression_tests.py"],
    args = ["--yaml-dir=tuned_examples/a3c"],
    data = ["tuned_examples/a3c/cartpole-a3c.yaml"],
    main = "tests/run_regression_tests.py",
    tags = [
        "learning_tests",
        "learning_tests_cartpole",
        "learning_tests_discrete",
        "team:ml",
    ],
)

# AlphaStar
py_test(
    name = "learning_tests_cartpole_alpha_star",
    size = "large",
    srcs = ["tests/run_regression_tests.py"],
    args = [
        "--yaml-dir=tuned_examples/alpha_star",
        "--num-cpus=20",
    ],
    data = ["tuned_examples/alpha_star/multi-agent-cartpole-alpha-star.yaml"],
    main = "tests/run_regression_tests.py",
    tags = [
        "learning_tests",
        "learning_tests_cartpole",
        "learning_tests_discrete",
        "team:ml",
    ],
)

# APEX-DQN
py_test(
    name = "learning_tests_cartpole_apex",
    size = "large",
    srcs = ["tests/run_regression_tests.py"],
    args = [
        "--yaml-dir=tuned_examples/dqn",
        "--num-cpus=6",
    ],
    data = [
        "tuned_examples/dqn/cartpole-apex.yaml",
    ],
    main = "tests/run_regression_tests.py",
    tags = [
        "learning_tests",
        "learning_tests_cartpole",
        "learning_tests_discrete",
        "team:ml",
    ],
)

# Once APEX supports multi-GPU.
# py_test(
#    name = "learning_cartpole_apex_fake_gpus",
#    main = "tests/run_regression_tests.py",
#    tags = ["team:ml", "learning_tests", "learning_tests_cartpole", "learning_tests_discrete", "fake_gpus"],
#    size = "large",
#    srcs = ["tests/run_regression_tests.py"],
#    data = ["tuned_examples/dqn/cartpole-apex-fake-gpus.yaml"],
#    args = ["--yaml-dir=tuned_examples/dqn"]
# )

# APPO
py_test(
    name = "learning_tests_cartpole_appo_no_vtrace",
    size = "large",
    srcs = ["tests/run_regression_tests.py"],
    args = ["--yaml-dir=tuned_examples/ppo"],
    data = ["tuned_examples/ppo/cartpole-appo.yaml"],
    main = "tests/run_regression_tests.py",
    tags = [
        "learning_tests",
        "learning_tests_cartpole",
        "learning_tests_discrete",
        "team:ml",
    ],
)

py_test(
    name = "learning_tests_cartpole_appo_vtrace",
    size = "large",
    srcs = ["tests/run_regression_tests.py"],
    args = ["--yaml-dir=tuned_examples/ppo"],
    data = ["tuned_examples/ppo/cartpole-appo-vtrace.yaml"],
    main = "tests/run_regression_tests.py",
    tags = [
        "learning_tests",
        "learning_tests_cartpole",
        "learning_tests_discrete",
        "team:ml",
    ],
)

py_test(
    name = "learning_tests_cartpole_separate_losses_appo",
    size = "large",
    srcs = ["tests/run_regression_tests.py"],
    args = ["--yaml-dir=tuned_examples/ppo"],
    data = [
        "tuned_examples/ppo/cartpole-appo-vtrace-separate-losses.yaml",
    ],
    main = "tests/run_regression_tests.py",
    tags = [
        "learning_tests",
        "learning_tests_cartpole",
        "learning_tests_discrete",
        "team:ml",
        "tf_only",
    ],
)

py_test(
    name = "learning_tests_frozenlake_appo",
    size = "large",
    srcs = ["tests/run_regression_tests.py"],
    args = ["--yaml-dir=tuned_examples/ppo"],
    data = ["tuned_examples/ppo/frozenlake-appo-vtrace.yaml"],
    main = "tests/run_regression_tests.py",
    tags = [
        "learning_tests",
        "learning_tests_discrete",
        "team:ml",
    ],
)

py_test(
    name = "learning_tests_cartpole_appo_fake_gpus",
    size = "large",
    srcs = ["tests/run_regression_tests.py"],
    args = ["--yaml-dir=tuned_examples/ppo"],
    data = ["tuned_examples/ppo/cartpole-appo-vtrace-fake-gpus.yaml"],
    main = "tests/run_regression_tests.py",
    tags = [
        "fake_gpus",
        "learning_tests",
        "learning_tests_cartpole",
        "learning_tests_discrete",
        "team:ml",
    ],
)

# ARS
py_test(
    name = "learning_tests_cartpole_ars",
    size = "large",
    srcs = ["tests/run_regression_tests.py"],
    args = ["--yaml-dir=tuned_examples/ars"],
    data = ["tuned_examples/ars/cartpole-ars.yaml"],
    main = "tests/run_regression_tests.py",
    tags = [
        "learning_tests",
        "learning_tests_cartpole",
        "learning_tests_discrete",
        "team:ml",
    ],
)

# CQL
py_test(
    name = "learning_tests_pendulum_cql",
    size = "large",
    srcs = ["tests/run_regression_tests.py"],
    args = ["--yaml-dir=tuned_examples/cql"],
    # Include the zipped json data file as well.
    data = [
        "tests/data/pendulum/enormous.zip",
        "tuned_examples/cql/pendulum-cql.yaml",
    ],
    main = "tests/run_regression_tests.py",
    tags = [
        "learning_tests",
        "learning_tests_continuous",
        "learning_tests_pendulum",
        "team:ml",
    ],
)

# DDPG
# py_test(
#    name = "learning_tests_pendulum_ddpg",
#    main = "tests/run_regression_tests.py",
#    tags = ["team:ml", "learning_tests", "learning_tests_pendulum", "learning_tests_continuous"],
#    size = "large",
#    srcs = ["tests/run_regression_tests.py"],
#    data = glob(["tuned_examples/ddpg/pendulum-ddpg.yaml"]),
#    args = ["--yaml-dir=tuned_examples/ddpg"]
# )

# py_test(
#    name = "learning_tests_pendulum_ddpg_fake_gpus",
#    main = "tests/run_regression_tests.py",
#    tags = ["team:ml", "learning_tests", "learning_tests_pendulum", "learning_tests_continuous", "fake_gpus"],
#    size = "large",
#    srcs = ["tests/run_regression_tests.py"],
#    data = ["tuned_examples/ddpg/pendulum-ddpg-fake-gpus.yaml"],
#    args = ["--yaml-dir=tuned_examples/ddpg"]
# )

# DDPPO
py_test(
    name = "learning_tests_cartpole_ddppo",
    size = "large",
    srcs = ["tests/run_regression_tests.py"],
    args = ["--yaml-dir=tuned_examples/ppo"],
    data = glob(["tuned_examples/ppo/cartpole-ddppo.yaml"]),
    main = "tests/run_regression_tests.py",
    tags = [
        "learning_tests",
        "learning_tests_cartpole",
        "learning_tests_discrete",
        "team:ml",
        "torch_only",
    ],
)

# DQN
py_test(
    name = "learning_tests_cartpole_dqn",
    size = "large",
    srcs = ["tests/run_regression_tests.py"],
    args = ["--yaml-dir=tuned_examples/dqn"],
    data = ["tuned_examples/dqn/cartpole-dqn.yaml"],
    main = "tests/run_regression_tests.py",
    tags = [
        "learning_tests",
        "learning_tests_cartpole",
        "learning_tests_discrete",
        "team:ml",
    ],
)

py_test(
    name = "learning_tests_cartpole_dqn_softq",
    size = "large",
    srcs = ["tests/run_regression_tests.py"],
    args = ["--yaml-dir=tuned_examples/dqn"],
    data = ["tuned_examples/dqn/cartpole-dqn-softq.yaml"],
    main = "tests/run_regression_tests.py",
    tags = [
        "learning_tests",
        "learning_tests_cartpole",
        "learning_tests_discrete",
        "team:ml",
    ],
)

# Does not work with tf-eager tracing due to Exploration's postprocessing
# method injecting a tensor into a new graph. Revisit when tf-eager tracing
# is better supported.
py_test(
    name = "learning_tests_cartpole_dqn_param_noise",
    size = "large",
    srcs = ["tests/run_regression_tests.py"],
    args = ["--yaml-dir=tuned_examples/dqn"],
    data = ["tuned_examples/dqn/cartpole-dqn-param-noise.yaml"],
    main = "tests/run_regression_tests.py",
    tags = [
        "learning_tests",
        "learning_tests_cartpole",
        "learning_tests_discrete",
        "no_tf_eager_tracing",
        "team:ml",
    ],
)

py_test(
    name = "learning_tests_cartpole_dqn_fake_gpus",
    size = "large",
    srcs = ["tests/run_regression_tests.py"],
    args = ["--yaml-dir=tuned_examples/dqn"],
    data = ["tuned_examples/dqn/cartpole-dqn-fake-gpus.yaml"],
    main = "tests/run_regression_tests.py",
    tags = [
        "fake_gpus",
        "learning_tests",
        "learning_tests_cartpole",
        "learning_tests_discrete",
        "team:ml",
    ],
)

# Simple-Q
py_test(
    name = "learning_tests_cartpole_simpleq",
    size = "large",
    srcs = ["tests/run_regression_tests.py"],
    args = ["--yaml-dir=tuned_examples/dqn"],
    data = [
        "tuned_examples/dqn/cartpole-simpleq.yaml",
    ],
    main = "tests/run_regression_tests.py",
    tags = [
        "learning_tests",
        "learning_tests_cartpole",
        "learning_tests_discrete",
        "team:ml",
    ],
)

py_test(
    name = "learning_tests_cartpole_simpleq_fake_gpus",
    size = "medium",
    srcs = ["tests/run_regression_tests.py"],
    args = ["--yaml-dir=tuned_examples/dqn"],
    data = ["tuned_examples/dqn/cartpole-simpleq-fake-gpus.yaml"],
    main = "tests/run_regression_tests.py",
    tags = [
        "fake_gpus",
        "learning_tests",
        "learning_tests_cartpole",
        "learning_tests_discrete",
        "team:ml",
    ],
)

# ES
py_test(
    name = "learning_tests_cartpole_es",
    size = "large",
    srcs = ["tests/run_regression_tests.py"],
    args = ["--yaml-dir=tuned_examples/es"],
    data = ["tuned_examples/es/cartpole-es.yaml"],
    main = "tests/run_regression_tests.py",
    tags = [
        "learning_tests",
        "learning_tests_cartpole",
        "learning_tests_discrete",
        "team:ml",
    ],
)

# IMPALA
py_test(
    name = "learning_tests_cartpole_impala",
    size = "large",
    srcs = ["tests/run_regression_tests.py"],
    args = ["--yaml-dir=tuned_examples/impala"],
    data = ["tuned_examples/impala/cartpole-impala.yaml"],
    main = "tests/run_regression_tests.py",
    tags = [
        "learning_tests",
        "learning_tests_cartpole",
        "learning_tests_discrete",
        "team:ml",
    ],
)

py_test(
    name = "learning_tests_cartpole_impala_fake_gpus",
    size = "large",
    srcs = ["tests/run_regression_tests.py"],
    args = ["--yaml-dir=tuned_examples/impala"],
    data = ["tuned_examples/impala/cartpole-impala-fake-gpus.yaml"],
    main = "tests/run_regression_tests.py",
    tags = [
        "fake_gpus",
        "learning_tests",
        "learning_tests_cartpole",
        "learning_tests_discrete",
        "team:ml",
    ],
)

# Working, but takes a long time to learn (>15min).
# Removed due to Higher API conflicts with Pytorch-Import tests
## MB-MPO
#py_test(
#    name = "learning_tests_pendulum_mbmpo",
#    main = "tests/run_regression_tests.py",
#    tags = ["team:ml", "torch_only", "learning_tests", "learning_tests_pendulum", "learning_tests_continuous"],
#    size = "large",
#    srcs = ["tests/run_regression_tests.py"],
#    data = ["tuned_examples/mbmpo/pendulum-mbmpo.yaml"],
#    args = ["--yaml-dir=tuned_examples/mbmpo"]
#)

# PG
py_test(
    name = "learning_tests_cartpole_pg",
    size = "large",
    srcs = ["tests/run_regression_tests.py"],
    args = ["--yaml-dir=tuned_examples/pg"],
    data = ["tuned_examples/pg/cartpole-pg.yaml"],
    main = "tests/run_regression_tests.py",
    tags = [
        "learning_tests",
        "learning_tests_cartpole",
        "learning_tests_discrete",
        "team:ml",
    ],
)

py_test(
    name = "learning_tests_cartpole_pg_fake_gpus",
    size = "large",
    srcs = ["tests/run_regression_tests.py"],
    args = ["--yaml-dir=tuned_examples/pg"],
    data = ["tuned_examples/pg/cartpole-pg-fake-gpus.yaml"],
    main = "tests/run_regression_tests.py",
    tags = [
        "fake_gpus",
        "learning_tests",
        "learning_tests_cartpole",
        "learning_tests_discrete",
        "team:ml",
    ],
)

# PPO
py_test(
    name = "learning_tests_cartpole_ppo",
    size = "large",
    srcs = ["tests/run_regression_tests.py"],
    args = ["--yaml-dir=tuned_examples/ppo"],
    data = ["tuned_examples/ppo/cartpole-ppo.yaml"],
    main = "tests/run_regression_tests.py",
    tags = [
        "learning_tests",
        "learning_tests_cartpole",
        "learning_tests_discrete",
        "team:ml",
    ],
)

py_test(
    name = "learning_tests_pendulum_ppo",
    size = "large",
    srcs = ["tests/run_regression_tests.py"],
    args = ["--yaml-dir=tuned_examples/ppo"],
    data = ["tuned_examples/ppo/pendulum-ppo.yaml"],
    main = "tests/run_regression_tests.py",
    tags = [
        "learning_tests",
        "learning_tests_continuous",
        "learning_tests_pendulum",
        "team:ml",
    ],
)

py_test(
    name = "learning_tests_transformed_actions_pendulum_ppo",
    size = "large",
    srcs = ["tests/run_regression_tests.py"],
    args = ["--yaml-dir=tuned_examples/ppo"],
    data = ["tuned_examples/ppo/pendulum-transformed-actions-ppo.yaml"],
    main = "tests/run_regression_tests.py",
    tags = [
        "learning_tests",
        "learning_tests_continuous",
        "learning_tests_pendulum",
        "team:ml",
    ],
)

py_test(
    name = "learning_tests_repeat_after_me_ppo",
    size = "large",
    srcs = ["tests/run_regression_tests.py"],
    args = ["--yaml-dir=tuned_examples/ppo"],
    data = ["tuned_examples/ppo/repeatafterme-ppo-lstm.yaml"],
    main = "tests/run_regression_tests.py",
    tags = [
        "learning_tests",
        "learning_tests_discrete",
        "team:ml",
    ],
)

py_test(
    name = "learning_tests_cartpole_ppo_fake_gpus",
    size = "large",
    srcs = ["tests/run_regression_tests.py"],
    args = ["--yaml-dir=tuned_examples/ppo"],
    data = ["tuned_examples/ppo/cartpole-ppo-fake-gpus.yaml"],
    main = "tests/run_regression_tests.py",
    tags = [
        "fake_gpus",
        "learning_tests",
        "learning_tests_cartpole",
        "learning_tests_discrete",
        "team:ml",
    ],
)

# QMIX
py_test(
    name = "learning_tests_two_step_game_qmix",
    size = "large",
    srcs = ["tests/run_regression_tests.py"],
    args = [
        "--yaml-dir=tuned_examples/qmix",
        "--framework=torch",
    ],
    data = ["tuned_examples/qmix/two-step-game-qmix.yaml"],
    main = "tests/run_regression_tests.py",
    tags = [
        "learning_tests",
        "learning_tests_discrete",
        "team:ml",
    ],
)

py_test(
    name = "learning_tests_two_step_game_qmix_vdn_mixer",
    size = "large",
    srcs = ["tests/run_regression_tests.py"],
    args = [
        "--yaml-dir=tuned_examples/qmix",
        "--framework=torch",
    ],
    data = ["tuned_examples/qmix/two-step-game-qmix-vdn-mixer.yaml"],
    main = "tests/run_regression_tests.py",
    tags = [
        "learning_tests",
        "learning_tests_discrete",
        "team:ml",
    ],
)

py_test(
    name = "learning_tests_two_step_game_qmix_no_mixer",
    size = "large",
    srcs = ["tests/run_regression_tests.py"],
    args = [
        "--yaml-dir=tuned_examples/qmix",
        "--framework=torch",
    ],
    data = ["tuned_examples/qmix/two-step-game-qmix-no-mixer.yaml"],
    main = "tests/run_regression_tests.py",
    tags = [
        "learning_tests",
        "learning_tests_discrete",
        "team:ml",
    ],
)

# R2D2
py_test(
    name = "learning_tests_stateless_cartpole_r2d2",
    size = "large",
    srcs = ["tests/run_regression_tests.py"],
    args = ["--yaml-dir=tuned_examples/dqn"],
    data = ["tuned_examples/dqn/stateless-cartpole-r2d2.yaml"],
    main = "tests/run_regression_tests.py",
    tags = [
        "learning_tests",
        "learning_tests_cartpole",
        "learning_tests_discrete",
        "team:ml",
    ],
)

py_test(
    name = "learning_tests_stateless_cartpole_r2d2_fake_gpus",
    size = "large",
    srcs = ["tests/run_regression_tests.py"],
    args = ["--yaml-dir=tuned_examples/dqn"],
    data = ["tuned_examples/dqn/stateless-cartpole-r2d2-fake-gpus.yaml"],
    main = "tests/run_regression_tests.py",
    tags = [
        "fake_gpus",
        "learning_tests",
        "learning_tests_cartpole",
        "team:ml",
    ],
)

# SAC
py_test(
    name = "learning_tests_cartpole_sac",
    size = "large",
    srcs = ["tests/run_regression_tests.py"],
    args = ["--yaml-dir=tuned_examples/sac"],
    data = ["tuned_examples/sac/cartpole-sac.yaml"],
    main = "tests/run_regression_tests.py",
    tags = [
        "learning_tests",
        "learning_tests_cartpole",
        "learning_tests_discrete",
        "team:ml",
    ],
)

py_test(
    name = "learning_tests_cartpole_continuous_pybullet_sac",
    size = "large",
    srcs = ["tests/run_regression_tests.py"],
    args = ["--yaml-dir=tuned_examples/sac"],
    data = ["tuned_examples/sac/cartpole-continuous-pybullet-sac.yaml"],
    main = "tests/run_regression_tests.py",
    tags = [
        "learning_tests",
        "learning_tests_cartpole",
        "learning_tests_continuous",
        "team:ml",
    ],
)

# py_test(
#    name = "learning_tests_pendulum_sac",
#    main = "tests/run_regression_tests.py",
#    tags = ["team:ml", "learning_tests", "learning_tests_pendulum", "learning_tests_continuous"],
#    size = "large",
#    srcs = ["tests/run_regression_tests.py"],
#    data = ["tuned_examples/sac/pendulum-sac.yaml"],
#    args = ["--yaml-dir=tuned_examples/sac"]
# )

# py_test(
#    name = "learning_tests_transformed_actions_pendulum_sac",
#    main = "tests/run_regression_tests.py",
#    tags = ["team:ml", "learning_tests", "learning_tests_pendulum", "learning_tests_continuous"],
#    size = "large",
#    srcs = ["tests/run_regression_tests.py"],
#    data = ["tuned_examples/sac/pendulum-transformed-actions-sac.yaml"],
#    args = ["--yaml-dir=tuned_examples/sac"]
# )

# py_test(
#    name = "learning_tests_pendulum_sac_fake_gpus",
#    main = "tests/run_regression_tests.py",
#    tags = ["team:ml", "learning_tests", "learning_tests_pendulum", "learning_tests_continuous", "fake_gpus"],
#    size = "large",
#    srcs = ["tests/run_regression_tests.py"],
#    data = ["tuned_examples/sac/pendulum-sac-fake-gpus.yaml"],
#    args = ["--yaml-dir=tuned_examples/sac"]
# )

# SlateQ
py_test(
    name = "learning_tests_interest_evolution_10_candidates_recsim_env_slateq",
    size = "large",
    srcs = ["tests/run_regression_tests.py"],
    args = ["--yaml-dir=tuned_examples/slateq"],
    data = ["tuned_examples/slateq/interest-evolution-10-candidates-recsim-env-slateq.yaml"],
    main = "tests/run_regression_tests.py",
    tags = [
        "learning_tests",
        "learning_tests_discrete",
        "team:ml",
    ],
)

py_test(
    name = "learning_tests_interest_evolution_10_candidates_recsim_env_slateq_fake_gpus",
    size = "large",
    srcs = ["tests/run_regression_tests.py"],
    args = ["--yaml-dir=tuned_examples/slateq"],
    data = ["tuned_examples/slateq/interest-evolution-10-candidates-recsim-env-slateq.yaml"],
    main = "tests/run_regression_tests.py",
    tags = [
        "fake_gpus",
        "learning_tests",
        "learning_tests_discrete",
        "team:ml",
    ],
)

# TD3
py_test(
    name = "learning_tests_pendulum_td3",
    size = "large",
    srcs = ["tests/run_regression_tests.py"],
    args = ["--yaml-dir=tuned_examples/ddpg"],
    data = ["tuned_examples/ddpg/pendulum-td3.yaml"],
    main = "tests/run_regression_tests.py",
    tags = [
        "learning_tests",
        "learning_tests_continuous",
        "learning_tests_pendulum",
        "team:ml",
    ],
)

# --------------------------------------------------------------------
# Agents (Compilation, Losses, simple agent functionality tests)
# rllib/agents/
#
# Tag: trainers_dir
# --------------------------------------------------------------------

# Generic (all Trainers)
py_test(
    name = "test_callbacks",
    size = "medium",
    srcs = ["agents/tests/test_callbacks.py"],
    tags = [
        "team:ml",
        "trainers_dir",
        "trainers_dir_generic",
    ],
)

py_test(
    name = "test_memory_leaks_generic",
    size = "large",
    srcs = ["agents/tests/test_memory_leaks.py"],
    main = "agents/tests/test_memory_leaks.py",
    tags = [
        "team:ml",
        "trainers_dir",
    ],
)

py_test(
    name = "test_trainer",
    size = "large",
    srcs = ["agents/tests/test_trainer.py"],
    tags = [
        "team:ml",
        "trainers_dir",
        "trainers_dir_generic",
    ],
)

py_test(
    name = "tests/test_worker_failures",
    size = "large",
    srcs = ["agents/tests/test_worker_failures.py"],
    tags = [
        "team:ml",
        "tests_dir",
        "trainers_dir_generic",
    ],
)

# Specific Trainers (Algorithms)
# A2/3CTrainer
py_test(
    name = "test_a2c",
    size = "large",
    srcs = ["agents/a3c/tests/test_a2c.py"],
    tags = [
        "team:ml",
        "trainers_dir",
    ],
)

py_test(
    name = "test_a3c",
    size = "large",
    srcs = ["agents/a3c/tests/test_a3c.py"],
    tags = [
        "team:ml",
        "trainers_dir",
    ],
)

# AlphaStar
py_test(
    name = "test_alpha_star",
    size = "large",
    srcs = ["agents/alpha_star/tests/test_alpha_star.py"],
    tags = [
        "team:ml",
        "trainers_dir",
    ],
)

# APEXTrainer (DQN)
py_test(
    name = "test_apex_dqn",
    size = "large",
    srcs = ["agents/dqn/tests/test_apex_dqn.py"],
    tags = [
        "team:ml",
        "trainers_dir",
    ],
)

# APEXDDPGTrainer
py_test(
    name = "test_apex_ddpg",
    size = "medium",
    srcs = ["agents/ddpg/tests/test_apex_ddpg.py"],
    tags = [
        "team:ml",
        "trainers_dir",
    ],
)

# ARS
py_test(
    name = "test_ars",
    size = "medium",
    srcs = ["agents/ars/tests/test_ars.py"],
    tags = [
        "team:ml",
        "trainers_dir",
    ],
)

# Bandits
py_test(
    name = "test_bandits",
    size = "medium",
    srcs = ["agents/bandit/tests/test_bandits.py"],
    tags = [
        "team:ml",
        "trainers_dir",
    ],
)

# CQLTrainer
py_test(
    name = "test_cql",
    size = "medium",
    srcs = ["agents/cql/tests/test_cql.py"],
    tags = [
        "team:ml",
        "trainers_dir",
    ],
)

# DDPGTrainer
py_test(
    name = "test_ddpg",
    size = "large",
    srcs = ["agents/ddpg/tests/test_ddpg.py"],
    tags = [
        "team:ml",
        "trainers_dir",
    ],
)

# DQNTrainer
py_test(
    name = "test_dqn",
    size = "large",
    srcs = ["agents/dqn/tests/test_dqn.py"],
    tags = [
        "team:ml",
        "trainers_dir",
    ],
)

# Dreamer
py_test(
    name = "test_dreamer",
    size = "small",
    srcs = ["agents/dreamer/tests/test_dreamer.py"],
    tags = [
        "team:ml",
        "trainers_dir",
    ],
)

# ES
py_test(
    name = "test_es",
    size = "medium",
    srcs = ["agents/es/tests/test_es.py"],
    tags = [
        "team:ml",
        "trainers_dir",
    ],
)

# IMPALA
py_test(
    name = "test_impala",
    size = "large",
    srcs = ["agents/impala/tests/test_impala.py"],
    tags = [
        "team:ml",
        "trainers_dir",
    ],
)

py_test(
    name = "test_vtrace",
    size = "small",
    srcs = ["agents/impala/tests/test_vtrace.py"],
    tags = [
        "team:ml",
        "trainers_dir",
    ],
)

# MARWILTrainer
py_test(
    name = "test_marwil",
    size = "large",
    srcs = ["agents/marwil/tests/test_marwil.py"],
    # Include the json data file.
    data = ["tests/data/cartpole/large.json"],
    tags = [
        "team:ml",
        "trainers_dir",
    ],
)

# BCTrainer (sub-type of MARWIL)
py_test(
    name = "test_bc",
    size = "large",
    srcs = ["agents/marwil/tests/test_bc.py"],
    # Include the json data file.
    data = ["tests/data/cartpole/large.json"],
    tags = [
        "team:ml",
        "trainers_dir",
    ],
)

# MAMLTrainer
py_test(
    name = "test_maml",
    size = "medium",
    srcs = ["agents/maml/tests/test_maml.py"],
    tags = [
        "team:ml",
        "trainers_dir",
    ],
)

# MBMPOTrainer
py_test(
    name = "test_mbmpo",
    size = "medium",
    srcs = ["agents/mbmpo/tests/test_mbmpo.py"],
    tags = [
        "team:ml",
        "trainers_dir",
    ],
)

# PGTrainer
py_test(
    name = "test_pg",
    size = "large",
    srcs = ["agents/pg/tests/test_pg.py"],
    tags = [
        "team:ml",
        "trainers_dir",
    ],
)

# PPOTrainer
py_test(
    name = "test_ppo",
    size = "large",
    srcs = ["agents/ppo/tests/test_ppo.py"],
    tags = [
        "team:ml",
        "trainers_dir",
    ],
)

# PPO: DDPPO
py_test(
    name = "test_ddppo",
    size = "medium",
    srcs = ["agents/ppo/tests/test_ddppo.py"],
    tags = [
        "team:ml",
        "trainers_dir",
    ],
)

# PPO: APPO
py_test(
    name = "test_appo",
    size = "large",
    srcs = ["agents/ppo/tests/test_appo.py"],
    tags = [
        "team:ml",
        "trainers_dir",
    ],
)

# QMixTrainer
py_test(
    name = "test_qmix",
    size = "medium",
    srcs = ["agents/qmix/tests/test_qmix.py"],
    tags = [
        "team:ml",
        "trainers_dir",
    ],
)

# R2D2Trainer
py_test(
    name = "test_r2d2",
    size = "large",
    srcs = ["agents/dqn/tests/test_r2d2.py"],
    tags = [
        "team:ml",
        "trainers_dir",
    ],
)

# RNNSACTrainer
py_test(
    name = "test_rnnsac",
    size = "medium",
    srcs = ["agents/sac/tests/test_rnnsac.py"],
    tags = [
        "team:ml",
        "trainers_dir",
    ],
)

# SACTrainer
py_test(
    name = "test_sac",
    size = "large",
    srcs = ["agents/sac/tests/test_sac.py"],
    tags = [
        "team:ml",
        "trainers_dir",
    ],
)

# SimpleQTrainer
py_test(
    name = "test_simple_q",
    size = "medium",
    srcs = ["agents/dqn/tests/test_simple_q.py"],
    tags = [
        "team:ml",
        "trainers_dir",
    ],
)

# SlateQTrainer
py_test(
    name = "test_slateq",
    size = "medium",
    srcs = ["agents/slateq/tests/test_slateq.py"],
    tags = [
        "team:ml",
        "trainers_dir",
    ],
)

# TD3Trainer
py_test(
    name = "test_td3",
    size = "large",
    srcs = ["agents/ddpg/tests/test_td3.py"],
    tags = [
        "team:ml",
        "trainers_dir",
    ],
)

# --------------------------------------------------------------------
# contrib Agents
# --------------------------------------------------------------------

py_test(
    name = "random_agent",
    size = "small",
    srcs = ["contrib/random_agent/random_agent.py"],
    main = "contrib/random_agent/random_agent.py",
    tags = [
        "team:ml",
        "trainers_dir",
    ],
)

py_test(
    name = "alpha_zero_cartpole",
    size = "large",
    srcs = ["contrib/alpha_zero/examples/train_cartpole.py"],
    args = [
        "--training-iteration=1",
        "--num-workers=2",
        "--ray-num-cpus=3",
    ],
    main = "contrib/alpha_zero/examples/train_cartpole.py",
    tags = [
        "team:ml",
        "trainers_dir",
    ],
)

# --------------------------------------------------------------------
# Memory leak tests
#
# Tag: memory_leak_tests
# --------------------------------------------------------------------

py_test(
    name = "test_memory_leak_a3c",
    size = "large",
    srcs = ["utils/tests/run_memory_leak_tests.py"],
    args = ["--yaml-dir=tuned_examples/a3c"],
    data = ["tuned_examples/a3c/memory-leak-test-a3c.yaml"],
    main = "utils/tests/run_memory_leak_tests.py",
    tags = [
        "memory_leak_tests",
        "team:ml",
    ],
)

py_test(
    name = "test_memory_leak_appo",
    size = "large",
    srcs = ["utils/tests/run_memory_leak_tests.py"],
    args = ["--yaml-dir=tuned_examples/ppo"],
    data = ["tuned_examples/ppo/memory-leak-test-appo.yaml"],
    main = "utils/tests/run_memory_leak_tests.py",
    tags = [
        "memory_leak_tests",
        "team:ml",
    ],
)

py_test(
    name = "test_memory_leak_ddpg",
    size = "large",
    srcs = ["utils/tests/run_memory_leak_tests.py"],
    args = ["--yaml-dir=tuned_examples/ddpg"],
    data = ["tuned_examples/ddpg/memory-leak-test-ddpg.yaml"],
    main = "utils/tests/run_memory_leak_tests.py",
    tags = [
        "memory_leak_tests",
        "team:ml",
    ],
)

py_test(
    name = "test_memory_leak_dqn",
    size = "large",
    srcs = ["utils/tests/run_memory_leak_tests.py"],
    args = ["--yaml-dir=tuned_examples/dqn"],
    data = ["tuned_examples/dqn/memory-leak-test-dqn.yaml"],
    main = "utils/tests/run_memory_leak_tests.py",
    tags = [
        "memory_leak_tests",
        "team:ml",
    ],
)

py_test(
    name = "test_memory_leak_impala",
    size = "large",
    srcs = ["utils/tests/run_memory_leak_tests.py"],
    args = ["--yaml-dir=tuned_examples/impala"],
    data = ["tuned_examples/impala/memory-leak-test-impala.yaml"],
    main = "utils/tests/run_memory_leak_tests.py",
    tags = [
        "memory_leak_tests",
        "team:ml",
    ],
)

py_test(
    name = "test_memory_leak_ppo",
    size = "large",
    srcs = ["utils/tests/run_memory_leak_tests.py"],
    args = ["--yaml-dir=tuned_examples/ppo"],
    data = ["tuned_examples/ppo/memory-leak-test-ppo.yaml"],
    main = "utils/tests/run_memory_leak_tests.py",
    tags = [
        "memory_leak_tests",
        "team:ml",
    ],
)

py_test(
    name = "test_memory_leak_sac",
    size = "large",
    srcs = ["utils/tests/run_memory_leak_tests.py"],
    args = ["--yaml-dir=tuned_examples/sac"],
    data = ["tuned_examples/sac/memory-leak-test-sac.yaml"],
    main = "utils/tests/run_memory_leak_tests.py",
    tags = [
        "memory_leak_tests",
        "team:ml",
    ],
)

# --------------------------------------------------------------------
# Agents (quick training test iterations via `rllib train`)
#
# Tag: quick_train
#
# These are not(!) learning tests, we only test here compilation and
# support for certain envs, spaces, setups.
# Should all be very short tests with label: "quick_train".
# --------------------------------------------------------------------

# A2C/A3C

py_test(
    name = "test_a3c_torch_pong_deterministic_v4",
    srcs = ["train.py"],
    args = [
        "--env",
        "PongDeterministic-v4",
        "--run",
        "A3C",
        "--stop",
        "'{\"training_iteration\": 1}'",
        "--config",
        "'{\"framework\": \"torch\", \"num_workers\": 2, \"sample_async\": false, \"model\": {\"use_lstm\": false, \"grayscale\": true, \"zero_mean\": false, \"dim\": 84}, \"preprocessor_pref\": \"rllib\"}'",
        "--ray-num-cpus",
        "4",
    ],
    main = "train.py",
    tags = [
        "quick_train",
        "team:ml",
    ],
)

py_test(
    name = "test_a3c_tf_pong_ram_v4",
    srcs = ["train.py"],
    args = [
        "--env",
        "Pong-ram-v4",
        "--run",
        "A3C",
        "--stop",
        "'{\"training_iteration\": 1}'",
        "--config",
        "'{\"framework\": \"tf\", \"num_workers\": 2}'",
        "--ray-num-cpus",
        "4",
    ],
    main = "train.py",
    tags = [
        "quick_train",
        "team:ml",
    ],
)

# DDPG/APEX-DDPG/TD3

py_test(
    name = "test_ddpg_mountaincar_continuous_v0_num_workers_0",
    srcs = ["train.py"],
    args = [
        "--env",
        "MountainCarContinuous-v0",
        "--run",
        "DDPG",
        "--stop",
        "'{\"training_iteration\": 1}'",
        "--config",
        "'{\"framework\": \"tf\", \"num_workers\": 0}'",
    ],
    main = "train.py",
    tags = [
        "quick_train",
        "team:ml",
    ],
)

py_test(
    name = "test_ddpg_mountaincar_continuous_v0_num_workers_1",
    srcs = ["train.py"],
    args = [
        "--env",
        "MountainCarContinuous-v0",
        "--run",
        "DDPG",
        "--stop",
        "'{\"training_iteration\": 1}'",
        "--config",
        "'{\"framework\": \"tf\", \"num_workers\": 1}'",
    ],
    main = "train.py",
    tags = [
        "quick_train",
        "team:ml",
    ],
)

py_test(
    name = "test_apex_ddpg_pendulum_v0_complete_episode_batches",
    srcs = ["train.py"],
    args = [
        "--env",
        "Pendulum-v1",
        "--run",
        "APEX_DDPG",
        "--stop",
        "'{\"training_iteration\": 1}'",
        "--config",
        "'{\"framework\": \"tf\", \"num_workers\": 2, \"optimizer\": {\"num_replay_buffer_shards\": 1}, \"learning_starts\": 100, \"min_time_s_per_reporting\": 1, \"batch_mode\": \"complete_episodes\"}'",
        "--ray-num-cpus",
        "4",
    ],
    main = "train.py",
    tags = [
        "quick_train",
        "team:ml",
    ],
)

# DQN/APEX

py_test(
    name = "test_dqn_frozenlake_v1",
    size = "small",
    srcs = ["train.py"],
    args = [
        "--env",
        "FrozenLake-v1",
        "--run",
        "DQN",
        "--config",
        "'{\"framework\": \"tf\"}'",
        "--stop",
        "'{\"training_iteration\": 1}'",
    ],
    main = "train.py",
    tags = [
        "quick_train",
        "team:ml",
    ],
)

py_test(
    name = "test_dqn_cartpole_v0_no_dueling",
    size = "small",
    srcs = ["train.py"],
    args = [
        "--env",
        "CartPole-v0",
        "--run",
        "DQN",
        "--stop",
        "'{\"training_iteration\": 1}'",
        "--config",
        "'{\"framework\": \"tf\", \"lr\": 1e-3, \"exploration_config\": {\"epsilon_timesteps\": 10000, \"final_epsilon\": 0.02}, \"dueling\": false, \"hiddens\": [], \"model\": {\"fcnet_hiddens\": [64], \"fcnet_activation\": \"relu\"}}'",
    ],
    main = "train.py",
    tags = [
        "quick_train",
        "team:ml",
    ],
)

py_test(
    name = "test_dqn_cartpole_v0",
    srcs = ["train.py"],
    args = [
        "--env",
        "CartPole-v0",
        "--run",
        "DQN",
        "--stop",
        "'{\"training_iteration\": 1}'",
        "--config",
        "'{\"framework\": \"tf\", \"num_workers\": 2}'",
        "--ray-num-cpus",
        "4",
    ],
    main = "train.py",
    tags = [
        "quick_train",
        "team:ml",
    ],
)

py_test(
    name = "test_dqn_cartpole_v0_with_offline_input_and_softq",
    size = "small",
    srcs = ["train.py"],
    args = [
        "--env",
        "CartPole-v0",
        "--run",
        "DQN",
        "--stop",
        "'{\"training_iteration\": 1}'",
        "--config",
        "'{\"framework\": \"tf\", \"input\": \"tests/data/cartpole\", \"learning_starts\": 0, \"input_evaluation\": [\"wis\", \"is\"], \"exploration_config\": {\"type\": \"SoftQ\"}}'",
    ],
    # Include the json data file.
    data = ["tests/data/cartpole/small.json"],
    main = "train.py",
    tags = [
        "external_files",
        "quick_train",
        "team:ml",
    ],
)

py_test(
    name = "test_dqn_pong_deterministic_v4",
    srcs = ["train.py"],
    args = [
        "--env",
        "PongDeterministic-v4",
        "--run",
        "DQN",
        "--stop",
        "'{\"training_iteration\": 1}'",
        "--config",
        "'{\"framework\": \"tf\", \"lr\": 1e-4, \"exploration_config\": {\"epsilon_timesteps\": 200000, \"final_epsilon\": 0.01}, \"buffer_size\": 10000, \"rollout_fragment_length\": 4, \"learning_starts\": 10000, \"target_network_update_freq\": 1000, \"gamma\": 0.99, \"prioritized_replay\": true}'",
    ],
    main = "train.py",
    tags = [
        "quick_train",
        "team:ml",
    ],
)

# IMPALA

py_test(
    name = "test_impala_buffers_2",
    srcs = ["train.py"],
    args = [
        "--env",
        "CartPole-v0",
        "--run",
        "IMPALA",
        "--stop",
        "'{\"training_iteration\": 1}'",
        "--config",
        "'{\"framework\": \"tf\", \"num_gpus\": 0, \"num_workers\": 2, \"min_time_s_per_reporting\": 1, \"num_multi_gpu_tower_stacks\": 2, \"replay_buffer_num_slots\": 100, \"replay_proportion\": 1.0}'",
        "--ray-num-cpus",
        "4",
    ],
    main = "train.py",
    tags = [
        "quick_train",
        "team:ml",
    ],
)

py_test(
    name = "test_impala_cartpole_v0_buffers_2_lstm",
    srcs = ["train.py"],
    args = [
        "--env",
        "CartPole-v0",
        "--run",
        "IMPALA",
        "--stop",
        "'{\"training_iteration\": 1}'",
        "--config",
        "'{\"framework\": \"tf\", \"num_gpus\": 0, \"num_workers\": 2, \"min_time_s_per_reporting\": 1, \"num_multi_gpu_tower_stacks\": 2, \"replay_buffer_num_slots\": 100, \"replay_proportion\": 1.0, \"model\": {\"use_lstm\": true}}'",
        "--ray-num-cpus",
        "4",
    ],
    main = "train.py",
    tags = [
        "quick_train",
        "team:ml",
    ],
)

py_test(
    name = "test_impala_pong_deterministic_v4_40k_ts_1G_obj_store",
    size = "medium",
    srcs = ["train.py"],
    args = [
        "--env",
        "PongDeterministic-v4",
        "--run",
        "IMPALA",
        "--stop",
        "'{\"timesteps_total\": 30000}'",
        "--ray-object-store-memory=1000000000",
        "--config",
        "'{\"framework\": \"tf\", \"num_workers\": 1, \"num_gpus\": 0, \"num_envs_per_worker\": 32, \"rollout_fragment_length\": 50, \"train_batch_size\": 50, \"learner_queue_size\": 1}'",
    ],
    main = "train.py",
    tags = [
        "quick_train",
        "team:ml",
    ],
)

# PG

py_test(
    name = "test_pg_tf_cartpole_v0_lstm",
    srcs = ["train.py"],
    args = [
        "--env",
        "CartPole-v0",
        "--run",
        "PG",
        "--stop",
        "'{\"training_iteration\": 1}'",
        "--config",
        "'{\"framework\": \"tf\", \"rollout_fragment_length\": 500, \"num_workers\": 1, \"model\": {\"use_lstm\": true, \"max_seq_len\": 100}}'",
    ],
    main = "train.py",
    tags = [
        "quick_train",
        "team:ml",
    ],
)

py_test(
    name = "test_pg_tf_cartpole_v0_multi_envs_per_worker",
    size = "small",
    srcs = ["train.py"],
    args = [
        "--env",
        "CartPole-v0",
        "--run",
        "PG",
        "--stop",
        "'{\"training_iteration\": 1}'",
        "--config",
        "'{\"framework\": \"tf\", \"rollout_fragment_length\": 500, \"num_workers\": 1, \"num_envs_per_worker\": 10}'",
    ],
    main = "train.py",
    tags = [
        "quick_train",
        "team:ml",
    ],
)

py_test(
    name = "test_pg_tf_pong_v0",
    srcs = ["train.py"],
    args = [
        "--env",
        "Pong-v0",
        "--run",
        "PG",
        "--stop",
        "'{\"training_iteration\": 1}'",
        "--config",
        "'{\"framework\": \"tf\", \"rollout_fragment_length\": 500, \"num_workers\": 1}'",
    ],
    main = "train.py",
    tags = [
        "quick_train",
        "team:ml",
    ],
)

# PPO/APPO

py_test(
    name = "test_ppo_tf_cartpole_v1_complete_episode_batches",
    srcs = ["train.py"],
    args = [
        "--env",
        "CartPole-v1",
        "--run",
        "PPO",
        "--stop",
        "'{\"training_iteration\": 1}'",
        "--config",
        "'{\"framework\": \"tf\", \"kl_coeff\": 1.0, \"num_sgd_iter\": 10, \"lr\": 1e-4, \"sgd_minibatch_size\": 64, \"train_batch_size\": 2000, \"num_workers\": 1, \"use_gae\": false, \"batch_mode\": \"complete_episodes\"}'",
    ],
    main = "train.py",
    tags = [
        "quick_train",
        "team:ml",
    ],
)

py_test(
    name = "test_ppo_tf_cartpole_v1_remote_worker_envs",
    srcs = ["train.py"],
    args = [
        "--env",
        "CartPole-v1",
        "--run",
        "PPO",
        "--stop",
        "'{\"training_iteration\": 1}'",
        "--config",
        "'{\"framework\": \"tf\", \"remote_worker_envs\": true, \"remote_env_batch_wait_ms\": 99999999, \"num_envs_per_worker\": 2, \"num_workers\": 1, \"train_batch_size\": 100, \"sgd_minibatch_size\": 50}'",
    ],
    main = "train.py",
    tags = [
        "quick_train",
        "team:ml",
    ],
)

py_test(
    name = "test_ppo_tf_cartpole_v1_remote_worker_envs_b",
    srcs = ["train.py"],
    args = [
        "--env",
        "CartPole-v1",
        "--run",
        "PPO",
        "--stop",
        "'{\"training_iteration\": 2}'",
        "--config",
        "'{\"framework\": \"tf\", \"remote_worker_envs\": true, \"num_envs_per_worker\": 2, \"num_workers\": 1, \"train_batch_size\": 100, \"sgd_minibatch_size\": 50}'",
    ],
    main = "train.py",
    tags = [
        "quick_train",
        "team:ml",
    ],
)

py_test(
    name = "test_appo_tf_pendulum_v1_no_gpus",
    srcs = ["train.py"],
    args = [
        "--env",
        "Pendulum-v1",
        "--run",
        "APPO",
        "--stop",
        "'{\"training_iteration\": 1}'",
        "--config",
        "'{\"framework\": \"tf\", \"num_workers\": 2, \"num_gpus\": 0}'",
        "--ray-num-cpus",
        "4",
    ],
    main = "train.py",
    tags = [
        "quick_train",
        "team:ml",
    ],
)

# --------------------------------------------------------------------
# Env tests
# rllib/env/
#
# Tag: env
# --------------------------------------------------------------------

sh_test(
    name = "env/tests/test_local_inference_cartpole",
    size = "medium",
    srcs = ["env/tests/test_policy_client_server_setup.sh"],
    args = [
        "local",
        "cartpole",
        "8800",
    ],
    data = glob(["examples/serving/*.py"]),
    tags = [
        "env",
        "team:ml",
    ],
)

sh_test(
    name = "env/tests/test_remote_inference_cartpole",
    size = "medium",
    srcs = ["env/tests/test_policy_client_server_setup.sh"],
    args = [
        "remote",
        "cartpole",
        "8810",
    ],
    data = glob(["examples/serving/*.py"]),
    tags = [
        "env",
        "team:ml",
    ],
)

sh_test(
    name = "env/tests/test_remote_inference_cartpole_lstm",
    size = "large",
    srcs = ["env/tests/test_policy_client_server_setup.sh"],
    args = [
        "remote",
        "cartpole_lstm",
        "8820",
    ],
    data = glob(["examples/serving/*.py"]),
    tags = [
        "env",
        "team:ml",
    ],
)

sh_test(
    name = "env/tests/test_local_inference_cartpole_w_2_concurrent_episodes",
    size = "medium",
    srcs = ["env/tests/test_policy_client_server_setup.sh"],
    args = [
        "local",
        "cartpole-dummy-2-episodes",
        "8830",
    ],
    data = glob(["examples/serving/*.py"]),
    tags = [
        "env",
        "team:ml",
    ],
)

sh_test(
    name = "env/tests/test_remote_inference_cartpole_w_2_concurrent_episodes",
    size = "medium",
    srcs = ["env/tests/test_policy_client_server_setup.sh"],
    args = [
        "remote",
        "cartpole-dummy-2-episodes",
        "8840",
    ],
    data = glob(["examples/serving/*.py"]),
    tags = [
        "env",
        "team:ml",
    ],
)

sh_test(
    name = "env/tests/test_local_inference_unity3d",
    size = "medium",
    srcs = ["env/tests/test_policy_client_server_setup.sh"],
    args = [
        "local",
        "unity3d",
        "8850",
    ],
    data = glob(["examples/serving/*.py"]),
    tags = [
        "env",
        "team:ml",
    ],
)

sh_test(
    name = "env/tests/test_remote_inference_unity3d",
    size = "medium",
    srcs = ["env/tests/test_policy_client_server_setup.sh"],
    args = [
        "remote",
        "unity3d",
        "8860",
    ],
    data = glob(["examples/serving/*.py"]),
    tags = [
        "env",
        "team:ml",
    ],
)

py_test(
    name = "env/tests/test_record_env_wrapper",
    size = "small",
    srcs = ["env/tests/test_record_env_wrapper.py"],
    tags = [
        "env",
        "team:ml",
    ],
)

py_test(
    name = "env/tests/test_remote_worker_envs",
    size = "medium",
    srcs = ["env/tests/test_remote_worker_envs.py"],
    tags = [
        "env",
        "team:ml",
    ],
)

py_test(
    name = "env/wrappers/tests/test_unity3d_env",
    size = "small",
    srcs = ["env/wrappers/tests/test_unity3d_env.py"],
    tags = [
        "env",
        "team:ml",
    ],
)

py_test(
    name = "env/wrappers/tests/test_recsim_wrapper",
    size = "small",
    srcs = ["env/wrappers/tests/test_recsim_wrapper.py"],
    tags = [
        "env",
        "team:ml",
    ],
)

py_test(
    name = "env/wrappers/tests/test_exception_wrapper",
    size = "small",
    srcs = ["env/wrappers/tests/test_exception_wrapper.py"],
    tags = [
        "env",
        "team:ml",
    ],
)

py_test(
    name = "env/wrappers/tests/test_group_agents_wrapper",
    size = "small",
    srcs = ["env/wrappers/tests/test_group_agents_wrapper.py"],
    tags = [
        "env",
        "team:ml",
    ],
)

# --------------------------------------------------------------------
# Evaluation components
# rllib/evaluation/
#
# Tag: evaluation
# --------------------------------------------------------------------

py_test(
    name = "evaluation/tests/test_postprocessing",
    size = "small",
    srcs = ["evaluation/tests/test_postprocessing.py"],
    tags = [
        "evaluation",
        "team:ml",
    ],
)

py_test(
    name = "evaluation/tests/test_rollout_worker",
    size = "medium",
    srcs = ["evaluation/tests/test_rollout_worker.py"],
    tags = [
        "evaluation",
        "team:ml",
    ],
)

py_test(
    name = "evaluation/tests/test_trajectory_view_api",
    size = "medium",
    srcs = ["evaluation/tests/test_trajectory_view_api.py"],
    tags = [
        "evaluation",
        "team:ml",
    ],
)

py_test(
    name = "evaluation/tests/test_episode",
    size = "small",
    srcs = ["evaluation/tests/test_episode.py"],
    tags = [
        "evaluation",
        "team:ml",
    ],
)

# --------------------------------------------------------------------
# Optimizers and Memories
# rllib/execution/
#
# Tag: execution
# --------------------------------------------------------------------

py_test(
    name = "test_segment_tree",
    size = "small",
    srcs = ["execution/tests/test_segment_tree.py"],
    tags = [
        "execution",
        "team:ml",
    ],
)

py_test(
    name = "test_prioritized_replay_buffer",
    size = "small",
    srcs = ["execution/tests/test_prioritized_replay_buffer.py"],
    tags = [
        "execution",
        "team:ml",
    ],
)

# --------------------------------------------------------------------
# Models and Distributions
# rllib/models/
#
# Tag: models
# --------------------------------------------------------------------

py_test(
    name = "test_attention_nets",
    size = "large",
    srcs = ["models/tests/test_attention_nets.py"],
    tags = [
        "models",
        "team:ml",
    ],
)

py_test(
    name = "test_conv2d_default_stacks",
    size = "medium",
    srcs = ["models/tests/test_conv2d_default_stacks.py"],
    tags = [
        "models",
        "team:ml",
    ],
)

py_test(
    name = "test_convtranspose2d_stack",
    size = "small",
    srcs = ["models/tests/test_convtranspose2d_stack.py"],
    data = glob(["tests/data/images/obstacle_tower.png"]),
    tags = [
        "models",
        "team:ml",
    ],
)

py_test(
    name = "test_distributions",
    size = "medium",
    srcs = ["models/tests/test_distributions.py"],
    tags = [
        "models",
        "team:ml",
    ],
)

py_test(
    name = "test_lstms",
    size = "large",
    srcs = ["models/tests/test_lstms.py"],
    tags = [
        "models",
        "team:ml",
    ],
)

py_test(
    name = "test_models",
    size = "medium",
    srcs = ["models/tests/test_models.py"],
    tags = [
        "models",
        "team:ml",
    ],
)

py_test(
    name = "test_preprocessors",
    size = "large",
    srcs = ["models/tests/test_preprocessors.py"],
    tags = [
        "models",
        "team:ml",
    ],
)

# --------------------------------------------------------------------
# Policies
# rllib/policy/
#
# Tag: policy
# --------------------------------------------------------------------

py_test(
    name = "policy/tests/test_compute_log_likelihoods",
    size = "medium",
    srcs = ["policy/tests/test_compute_log_likelihoods.py"],
    tags = [
        "policy",
        "team:ml",
    ],
)

py_test(
    name = "policy/tests/test_multi_agent_batch",
    size = "small",
    srcs = ["policy/tests/test_multi_agent_batch.py"],
    tags = [
        "policy",
        "team:ml",
    ],
)

py_test(
    name = "policy/tests/test_policy",
    size = "medium",
    srcs = ["policy/tests/test_policy.py"],
    tags = [
        "policy",
        "team:ml",
    ],
)

py_test(
    name = "policy/tests/test_rnn_sequencing",
    size = "small",
    srcs = ["policy/tests/test_rnn_sequencing.py"],
    tags = [
        "policy",
        "team:ml",
    ],
)

py_test(
    name = "policy/tests/test_sample_batch",
    size = "small",
    srcs = ["policy/tests/test_sample_batch.py"],
    tags = [
        "policy",
        "team:ml",
    ],
)

# --------------------------------------------------------------------
# Utils:
# rllib/utils/
#
# Tag: utils
# --------------------------------------------------------------------

py_test(
    name = "test_curiosity",
    size = "large",
    srcs = ["utils/exploration/tests/test_curiosity.py"],
    tags = [
        "team:ml",
        "utils",
    ],
)

py_test(
    name = "test_explorations",
    size = "large",
    srcs = ["utils/exploration/tests/test_explorations.py"],
    tags = [
        "team:ml",
        "utils",
    ],
)

py_test(
    name = "test_parameter_noise",
    size = "medium",
    srcs = ["utils/exploration/tests/test_parameter_noise.py"],
    tags = [
        "team:ml",
        "utils",
    ],
)

py_test(
    name = "test_random_encoder",
    size = "large",
    srcs = ["utils/exploration/tests/test_random_encoder.py"],
    tags = [
        "team:ml",
        "utils",
    ],
)

# Schedules
py_test(
    name = "test_schedules",
    size = "small",
    srcs = ["utils/schedules/tests/test_schedules.py"],
    tags = [
        "team:ml",
        "utils",
    ],
)

py_test(
    name = "test_framework_agnostic_components",
    size = "small",
    srcs = ["utils/tests/test_framework_agnostic_components.py"],
    data = glob(["utils/tests/**"]),
    tags = [
        "team:ml",
        "utils",
    ],
)

# Spaces/Space utils.
py_test(
    name = "test_space_utils",
    size = "large",
    srcs = ["utils/spaces/tests/test_space_utils.py"],
    tags = [
        "team:ml",
        "utils",
    ],
)

# TaskPool
py_test(
    name = "test_taskpool",
    size = "small",
    srcs = ["utils/tests/test_taskpool.py"],
    tags = [
        "team:ml",
        "utils",
    ],
)

# ReplayBuffers
py_test(
    name = "test_multi_agent_mixin_replay_buffer",
    size = "small",
    srcs = ["utils/replay_buffers/tests/test_multi_agent_mixin_replay_buffer.py"],
    tags = [
        "team:ml",
        "utils",
    ],
)

py_test(
    name = "test_multi_agent_prioritized_replay_buffer",
    size = "small",
    srcs = ["utils/replay_buffers/tests/test_multi_agent_prioritized_replay_buffer.py"],
    tags = [
        "team:ml",
        "utils",
    ],
)

py_test(
    name = "test_multi_agent_replay_buffer",
    size = "small",
    srcs = ["utils/replay_buffers/tests/test_multi_agent_replay_buffer.py"],
    tags = [
        "team:ml",
        "utils",
    ],
)

py_test(
    name = "test_prioritized_replay_buffer_replay_buffer_api",
    size = "small",
    srcs = ["utils/replay_buffers/tests/test_prioritized_replay_buffer_replay_buffer_api.py"],
    tags = [
        "team:ml",
        "utils",
    ],
)

py_test(
    name = "test_replay_buffer",
    size = "small",
    srcs = ["utils/replay_buffers/tests/test_replay_buffer.py"],
    tags = [
        "team:ml",
        "utils",
    ],
)

py_test(
    name = "test_reservoir_buffer",
    size = "small",
    srcs = ["utils/replay_buffers/tests/test_reservoir_buffer.py"],
    tags = [
        "team:ml",
        "utils",
    ],
)

py_test(
    name = "test_segment_tree_replay_buffer_api",
    size = "small",
    srcs = ["utils/replay_buffers/tests/test_segment_tree_replay_buffer_api.py"],
    tags = [
        "team:ml",
        "utils",
    ],
)

# --------------------------------------------------------------------
# rllib/tests/ directory
#
# Tag: tests_dir, tests_dir_[A-Z]
#
# NOTE: Add tests alphabetically into this list and make sure, to tag
# it correctly by its starting letter, e.g. tags=["tests_dir", "tests_dir_A"]
# for `tests/test_all_stuff.py`.
# --------------------------------------------------------------------

py_test(
    name = "tests/test_catalog",
    size = "medium",
    srcs = ["tests/test_catalog.py"],
    tags = [
        "team:ml",
        "tests_dir",
        "tests_dir_C",
    ],
)

py_test(
    name = "tests/test_checkpoint_restore_pg",
    size = "large",
    srcs = ["tests/test_checkpoint_restore.py"],
    args = ["TestCheckpointRestorePG"],
    main = "tests/test_checkpoint_restore.py",
    tags = [
        "team:ml",
        "tests_dir",
        "tests_dir_C",
    ],
)

py_test(
    name = "tests/test_checkpoint_restore_off_policy",
    size = "large",
    srcs = ["tests/test_checkpoint_restore.py"],
    args = ["TestCheckpointRestoreOffPolicy"],
    main = "tests/test_checkpoint_restore.py",
    tags = [
        "team:ml",
        "tests_dir",
        "tests_dir_C",
    ],
)

py_test(
    name = "tests/test_checkpoint_restore_evolution_algos",
    size = "large",
    srcs = ["tests/test_checkpoint_restore.py"],
    args = ["TestCheckpointRestoreEvolutionAlgos"],
    main = "tests/test_checkpoint_restore.py",
    tags = [
        "team:ml",
        "tests_dir",
        "tests_dir_C",
    ],
)

py_test(
    name = "tests/test_dependency_tf",
    size = "small",
    srcs = ["tests/test_dependency_tf.py"],
    tags = [
        "team:ml",
        "tests_dir",
        "tests_dir_D",
    ],
)

py_test(
    name = "tests/test_dependency_torch",
    size = "small",
    srcs = ["tests/test_dependency_torch.py"],
    tags = [
        "team:ml",
        "tests_dir",
        "tests_dir_D",
    ],
)

py_test(
    name = "tests/test_eager_support_pg",
    size = "large",
    srcs = ["tests/test_eager_support.py"],
    args = ["TestEagerSupportPG"],
    main = "tests/test_eager_support.py",
    tags = [
        "team:ml",
        "tests_dir",
        "tests_dir_E",
    ],
)

py_test(
    name = "tests/test_eager_support_off_policy",
    size = "large",
    srcs = ["tests/test_eager_support.py"],
    args = ["TestEagerSupportOffPolicy"],
    main = "tests/test_eager_support.py",
    tags = [
        "team:ml",
        "tests_dir",
        "tests_dir_E",
    ],
)

py_test(
    name = "test_env_with_subprocess",
    size = "medium",
    srcs = ["tests/test_env_with_subprocess.py"],
    main = "tests/test_env_with_subprocess.py",
    tags = [
        "team:ml",
        "tests_dir",
        "tests_dir_E",
    ],
)

py_test(
    name = "tests/test_exec_api",
    size = "medium",
    srcs = ["tests/test_exec_api.py"],
    tags = [
        "team:ml",
        "tests_dir",
        "tests_dir_E",
    ],
)

py_test(
    name = "tests/test_execution",
    size = "medium",
    srcs = ["tests/test_execution.py"],
    tags = [
        "team:ml",
        "tests_dir",
        "tests_dir_E",
    ],
)

py_test(
    name = "tests/test_export",
    size = "medium",
    srcs = ["tests/test_export.py"],
    tags = [
        "team:ml",
        "tests_dir",
        "tests_dir_E",
    ],
)

py_test(
    name = "tests/test_external_env",
    size = "large",
    srcs = ["tests/test_external_env.py"],
    tags = [
        "team:ml",
        "tests_dir",
        "tests_dir_E",
    ],
)

py_test(
    name = "tests/test_external_multi_agent_env",
    size = "medium",
    srcs = ["tests/test_external_multi_agent_env.py"],
    tags = [
        "team:ml",
        "tests_dir",
        "tests_dir_E",
    ],
)

py_test(
    name = "tests/test_filters",
    size = "small",
    srcs = ["tests/test_filters.py"],
    tags = [
        "team:ml",
        "tests_dir",
        "tests_dir_F",
    ],
)

py_test(
    name = "tests/test_gpus",
    size = "large",
    srcs = ["tests/test_gpus.py"],
    tags = [
        "team:ml",
        "tests_dir",
        "tests_dir_G",
    ],
)

py_test(
    name = "tests/test_io",
    size = "large",
    srcs = ["tests/test_io.py"],
    tags = [
        "team:ml",
        "tests_dir",
        "tests_dir_I",
    ],
)

py_test(
    name = "tests/test_local",
    size = "medium",
    srcs = ["tests/test_local.py"],
    tags = [
        "team:ml",
        "tests_dir",
        "tests_dir_L",
    ],
)

py_test(
    name = "tests/test_lstm",
    size = "medium",
    srcs = ["tests/test_lstm.py"],
    tags = [
        "team:ml",
        "tests_dir",
        "tests_dir_L",
    ],
)

py_test(
    name = "tests/test_model_imports",
    size = "medium",
    srcs = ["tests/test_model_imports.py"],
    data = glob(["tests/data/model_weights/**"]),
    tags = [
        "model_imports",
        "team:ml",
        "tests_dir",
        "tests_dir_M",
    ],
)

py_test(
    name = "tests/test_multi_agent_env",
    size = "medium",
    srcs = ["tests/test_multi_agent_env.py"],
    tags = [
        "team:ml",
        "tests_dir",
        "tests_dir_M",
    ],
)

py_test(
    name = "tests/test_multi_agent_pendulum",
    size = "large",
    srcs = ["tests/test_multi_agent_pendulum.py"],
    tags = [
        "team:ml",
        "tests_dir",
        "tests_dir_M",
    ],
)

py_test(
    name = "tests/test_nested_action_spaces",
    size = "medium",
    srcs = ["tests/test_nested_action_spaces.py"],
    main = "tests/test_nested_action_spaces.py",
    tags = [
        "team:ml",
        "tests_dir",
        "tests_dir_N",
    ],
)

py_test(
    name = "tests/test_nested_observation_spaces",
    size = "medium",
    srcs = ["tests/test_nested_observation_spaces.py"],
    main = "tests/test_nested_observation_spaces.py",
    tags = [
        "team:ml",
        "tests_dir",
        "tests_dir_N",
    ],
)

py_test(
    name = "tests/test_nn_framework_import_errors",
    size = "small",
    srcs = ["tests/test_nn_framework_import_errors.py"],
    tags = [
        "team:ml",
        "tests_dir",
        "tests_dir_N",
    ],
)

py_test(
    name = "tests/test_pettingzoo_env",
    size = "medium",
    srcs = ["tests/test_pettingzoo_env.py"],
    tags = [
        "team:ml",
        "tests_dir",
        "tests_dir_P",
    ],
)

py_test(
    name = "tests/test_placement_groups",
    size = "medium",
    srcs = ["tests/test_placement_groups.py"],
    tags = [
        "team:ml",
        "tests_dir",
        "tests_dir_P",
    ],
)

py_test(
    name = "tests/test_ray_client",
    size = "large",
    srcs = ["tests/test_ray_client.py"],
    tags = [
        "team:ml",
        "tests_dir",
        "tests_dir_R",
    ],
)

py_test(
    name = "tests/test_reproducibility",
    size = "medium",
    srcs = ["tests/test_reproducibility.py"],
    tags = [
        "team:ml",
        "tests_dir",
        "tests_dir_R",
    ],
)

# Test [train|evaluate].py scripts (w/o confirming evaluation performance).
py_test(
    name = "test_rllib_evaluate_1",
    size = "large",
    srcs = ["tests/test_rllib_train_and_evaluate.py"],
    args = ["TestEvaluate1"],
    data = [
        "evaluate.py",
        "train.py",
    ],
    main = "tests/test_rllib_train_and_evaluate.py",
    tags = [
        "team:ml",
        "tests_dir",
        "tests_dir_R",
    ],
)

py_test(
    name = "test_rllib_evaluate_2",
    size = "large",
    srcs = ["tests/test_rllib_train_and_evaluate.py"],
    args = ["TestEvaluate2"],
    data = [
        "evaluate.py",
        "train.py",
    ],
    main = "tests/test_rllib_train_and_evaluate.py",
    tags = [
        "team:ml",
        "tests_dir",
        "tests_dir_R",
    ],
)

py_test(
    name = "test_rllib_evaluate_3",
    size = "large",
    srcs = ["tests/test_rllib_train_and_evaluate.py"],
    args = ["TestEvaluate3"],
    data = [
        "evaluate.py",
        "train.py",
    ],
    main = "tests/test_rllib_train_and_evaluate.py",
    tags = [
        "team:ml",
        "tests_dir",
        "tests_dir_R",
    ],
)

py_test(
    name = "test_rllib_evaluate_4",
    size = "large",
    srcs = ["tests/test_rllib_train_and_evaluate.py"],
    args = ["TestEvaluate4"],
    data = [
        "evaluate.py",
        "train.py",
    ],
    main = "tests/test_rllib_train_and_evaluate.py",
    tags = [
        "team:ml",
        "tests_dir",
        "tests_dir_R",
    ],
)

# Test [train|evaluate].py scripts (and confirm `rllib evaluate` performance is same
# as the final one from the `rllib train` run).
py_test(
    name = "test_rllib_train_and_evaluate",
    size = "large",
    srcs = ["tests/test_rllib_train_and_evaluate.py"],
    args = ["TestTrainAndEvaluate"],
    data = [
        "evaluate.py",
        "train.py",
    ],
    main = "tests/test_rllib_train_and_evaluate.py",
    tags = [
        "team:ml",
        "tests_dir",
        "tests_dir_R",
    ],
)

py_test(
    name = "tests/test_supported_multi_agent_pg",
    size = "medium",
    srcs = ["tests/test_supported_multi_agent.py"],
    args = ["TestSupportedMultiAgentPG"],
    main = "tests/test_supported_multi_agent.py",
    tags = [
        "team:ml",
        "tests_dir",
        "tests_dir_S",
    ],
)

py_test(
    name = "tests/test_supported_multi_agent_off_policy",
    size = "medium",
    srcs = ["tests/test_supported_multi_agent.py"],
    args = ["TestSupportedMultiAgentOffPolicy"],
    main = "tests/test_supported_multi_agent.py",
    tags = [
        "team:ml",
        "tests_dir",
        "tests_dir_S",
    ],
)

py_test(
    name = "tests/test_supported_spaces_pg",
    size = "large",
    srcs = ["tests/test_supported_spaces.py"],
    args = ["TestSupportedSpacesPG"],
    main = "tests/test_supported_spaces.py",
    tags = [
        "team:ml",
        "tests_dir",
        "tests_dir_S",
    ],
)

py_test(
    name = "tests/test_supported_spaces_off_policy",
    size = "medium",
    srcs = ["tests/test_supported_spaces.py"],
    args = ["TestSupportedSpacesOffPolicy"],
    main = "tests/test_supported_spaces.py",
    tags = [
        "team:ml",
        "tests_dir",
        "tests_dir_S",
    ],
)

py_test(
    name = "tests/test_supported_spaces_evolution_algos",
    size = "large",
    srcs = ["tests/test_supported_spaces.py"],
    args = ["TestSupportedSpacesEvolutionAlgos"],
    main = "tests/test_supported_spaces.py",
    tags = [
        "team:ml",
        "tests_dir",
        "tests_dir_S",
    ],
)

py_test(
    name = "tests/test_timesteps",
    size = "small",
    srcs = ["tests/test_timesteps.py"],
    tags = [
        "team:ml",
        "tests_dir",
        "tests_dir_T",
    ],
)

# --------------------------------------------------------------------
# examples/ directory (excluding examples/documentation/...)
#
# Tag: examples, examples_[A-Z]
#
# NOTE: Add tests alphabetically into this list and make sure, to tag
# it correctly by its starting letter, e.g. tags=["examples", "examples_A"]
# for `examples/all_stuff.py`.
# --------------------------------------------------------------------

py_test(
    name = "examples/action_masking_tf",
    size = "medium",
    srcs = ["examples/action_masking.py"],
    args = ["--stop-iter=2"],
    main = "examples/action_masking.py",
    tags = [
        "examples",
        "examples_A",
        "team:ml",
    ],
)

py_test(
    name = "examples/action_masking_torch",
    size = "medium",
    srcs = ["examples/action_masking.py"],
    args = [
        "--stop-iter=2",
        "--framework=torch",
    ],
    main = "examples/action_masking.py",
    tags = [
        "examples",
        "examples_A",
        "team:ml",
    ],
)

py_test(
    name = "examples/attention_net_tf",
    size = "medium",
    srcs = ["examples/attention_net.py"],
    args = [
        "--as-test",
        "--stop-reward=70",
    ],
    main = "examples/attention_net.py",
    tags = [
        "examples",
        "examples_A",
        "team:ml",
    ],
)

py_test(
    name = "examples/attention_net_torch",
    size = "medium",
    srcs = ["examples/attention_net.py"],
    args = [
        "--as-test",
        "--stop-reward=70",
        "--framework torch",
    ],
    main = "examples/attention_net.py",
    tags = [
        "examples",
        "examples_A",
        "team:ml",
    ],
)

py_test(
    name = "examples/autoregressive_action_dist_tf",
    size = "medium",
    srcs = ["examples/autoregressive_action_dist.py"],
    args = [
        "--as-test",
        "--stop-reward=150",
        "--num-cpus=4",
    ],
    main = "examples/autoregressive_action_dist.py",
    tags = [
        "examples",
        "examples_A",
        "team:ml",
    ],
)

py_test(
    name = "examples/autoregressive_action_dist_torch",
    size = "medium",
    srcs = ["examples/autoregressive_action_dist.py"],
    args = [
        "--as-test",
        "--framework=torch",
        "--stop-reward=150",
        "--num-cpus=4",
    ],
    main = "examples/autoregressive_action_dist.py",
    tags = [
        "examples",
        "examples_A",
        "team:ml",
    ],
)

py_test(
    name = "examples/bare_metal_policy_with_custom_view_reqs",
    size = "medium",
    srcs = ["examples/bare_metal_policy_with_custom_view_reqs.py"],
    main = "examples/bare_metal_policy_with_custom_view_reqs.py",
    tags = [
        "examples",
        "examples_B",
        "team:ml",
    ],
)

py_test(
    name = "examples/batch_norm_model_ppo_tf",
    size = "medium",
    srcs = ["examples/batch_norm_model.py"],
    args = [
        "--as-test",
        "--run=PPO",
        "--stop-reward=80",
    ],
    main = "examples/batch_norm_model.py",
    tags = [
        "examples",
        "examples_B",
        "team:ml",
    ],
)

py_test(
    name = "examples/batch_norm_model_ppo_torch",
    size = "medium",
    srcs = ["examples/batch_norm_model.py"],
    args = [
        "--as-test",
        "--framework=torch",
        "--run=PPO",
        "--stop-reward=80",
    ],
    main = "examples/batch_norm_model.py",
    tags = [
        "examples",
        "examples_B",
        "team:ml",
    ],
)

py_test(
    name = "examples/batch_norm_model_dqn_tf",
    size = "medium",
    srcs = ["examples/batch_norm_model.py"],
    args = [
        "--as-test",
        "--run=DQN",
        "--stop-reward=70",
    ],
    main = "examples/batch_norm_model.py",
    tags = [
        "examples",
        "examples_B",
        "team:ml",
    ],
)

py_test(
    name = "examples/batch_norm_model_dqn_torch",
    size = "large",  # DQN learns much slower with BatchNorm.
    srcs = ["examples/batch_norm_model.py"],
    args = [
        "--as-test",
        "--framework=torch",
        "--run=DQN",
        "--stop-reward=70",
    ],
    main = "examples/batch_norm_model.py",
    tags = [
        "examples",
        "examples_B",
        "team:ml",
    ],
)

py_test(
    name = "examples/batch_norm_model_ddpg_tf",
    size = "medium",
    srcs = ["examples/batch_norm_model.py"],
    args = [
        "--run=DDPG",
        "--stop-iters=1",
    ],
    main = "examples/batch_norm_model.py",
    tags = [
        "examples",
        "examples_B",
        "team:ml",
    ],
)

py_test(
    name = "examples/batch_norm_model_ddpg_torch",
    size = "medium",
    srcs = ["examples/batch_norm_model.py"],
    args = [
        "--framework=torch",
        "--run=DDPG",
        "--stop-iters=1",
    ],
    main = "examples/batch_norm_model.py",
    tags = [
        "examples",
        "examples_B",
        "team:ml",
    ],
)

py_test(
    name = "examples/cartpole_lstm_impala_tf",
    size = "medium",
    srcs = ["examples/cartpole_lstm.py"],
    args = [
        "--as-test",
        "--run=IMPALA",
        "--stop-reward=40",
        "--num-cpus=4",
    ],
    main = "examples/cartpole_lstm.py",
    tags = [
        "examples",
        "examples_C",
        "examples_C_AtoT",
        "team:ml",
    ],
)

py_test(
    name = "examples/cartpole_lstm_impala_torch",
    size = "medium",
    srcs = ["examples/cartpole_lstm.py"],
    args = [
        "--as-test",
        "--framework=torch",
        "--run=IMPALA",
        "--stop-reward=40",
        "--num-cpus=4",
    ],
    main = "examples/cartpole_lstm.py",
    tags = [
        "examples",
        "examples_C",
        "examples_C_AtoT",
        "team:ml",
    ],
)

py_test(
    name = "examples/cartpole_lstm_ppo_tf",
    size = "medium",
    srcs = ["examples/cartpole_lstm.py"],
    args = [
        "--as-test",
        "--framework=tf",
        "--run=PPO",
        "--stop-reward=40",
        "--num-cpus=4",
    ],
    main = "examples/cartpole_lstm.py",
    tags = [
        "examples",
        "examples_C",
        "examples_C_AtoT",
        "team:ml",
    ],
)

py_test(
    name = "examples/cartpole_lstm_ppo_tf2",
    size = "large",
    srcs = ["examples/cartpole_lstm.py"],
    args = [
        "--as-test",
        "--framework=tf2",
        "--run=PPO",
        "--stop-reward=40",
        "--num-cpus=4",
    ],
    main = "examples/cartpole_lstm.py",
    tags = [
        "examples",
        "examples_C",
        "examples_C_AtoT",
        "team:ml",
    ],
)

py_test(
    name = "examples/cartpole_lstm_ppo_torch",
    size = "medium",
    srcs = ["examples/cartpole_lstm.py"],
    args = [
        "--as-test",
        "--framework=torch",
        "--run=PPO",
        "--stop-reward=40",
        "--num-cpus=4",
    ],
    main = "examples/cartpole_lstm.py",
    tags = [
        "examples",
        "examples_C",
        "examples_C_AtoT",
        "team:ml",
    ],
)

py_test(
    name = "examples/cartpole_lstm_ppo_tf_with_prev_a_and_r",
    size = "medium",
    srcs = ["examples/cartpole_lstm.py"],
    args = [
        "--as-test",
        "--run=PPO",
        "--stop-reward=40",
        "--use-prev-action",
        "--use-prev-reward",
        "--num-cpus=4",
    ],
    main = "examples/cartpole_lstm.py",
    tags = [
        "examples",
        "examples_C",
        "examples_C_AtoT",
        "team:ml",
    ],
)

py_test(
    name = "examples/centralized_critic_tf",
    size = "large",
    srcs = ["examples/centralized_critic.py"],
    args = [
        "--as-test",
        "--stop-reward=7.2",
    ],
    main = "examples/centralized_critic.py",
    tags = [
        "examples",
        "examples_C",
        "examples_C_AtoT",
        "team:ml",
    ],
)

py_test(
    name = "examples/centralized_critic_torch",
    size = "large",
    srcs = ["examples/centralized_critic.py"],
    args = [
        "--as-test",
        "--framework=torch",
        "--stop-reward=7.2",
    ],
    main = "examples/centralized_critic.py",
    tags = [
        "examples",
        "examples_C",
        "examples_C_AtoT",
        "team:ml",
    ],
)

py_test(
    name = "examples/centralized_critic_2_tf",
    size = "medium",
    srcs = ["examples/centralized_critic_2.py"],
    args = [
        "--as-test",
        "--stop-reward=6.0",
    ],
    main = "examples/centralized_critic_2.py",
    tags = [
        "examples",
        "examples_C",
        "examples_C_AtoT",
        "team:ml",
    ],
)

py_test(
    name = "examples/centralized_critic_2_torch",
    size = "medium",
    srcs = ["examples/centralized_critic_2.py"],
    args = [
        "--as-test",
        "--framework=torch",
        "--stop-reward=6.0",
    ],
    main = "examples/centralized_critic_2.py",
    tags = [
        "examples",
        "examples_C",
        "examples_C_AtoT",
        "team:ml",
    ],
)

py_test(
    name = "examples/checkpoint_by_custom_criteria",
    size = "medium",
    srcs = ["examples/checkpoint_by_custom_criteria.py"],
    args = ["--stop-iters=3 --num-cpus=3"],
    main = "examples/checkpoint_by_custom_criteria.py",
    tags = [
        "examples",
        "examples_C",
        "examples_C_AtoT",
        "team:ml",
    ],
)

py_test(
    name = "examples/complex_struct_space_tf",
    size = "medium",
    srcs = ["examples/complex_struct_space.py"],
    args = ["--framework=tf"],
    main = "examples/complex_struct_space.py",
    tags = [
        "examples",
        "examples_C",
        "examples_C_AtoT",
        "team:ml",
    ],
)

py_test(
    name = "examples/complex_struct_space_tf_eager",
    size = "medium",
    srcs = ["examples/complex_struct_space.py"],
    args = ["--framework=tfe"],
    main = "examples/complex_struct_space.py",
    tags = [
        "examples",
        "examples_C",
        "examples_C_AtoT",
        "team:ml",
    ],
)

py_test(
    name = "examples/complex_struct_space_torch",
    size = "medium",
    srcs = ["examples/complex_struct_space.py"],
    args = ["--framework=torch"],
    main = "examples/complex_struct_space.py",
    tags = [
        "examples",
        "examples_C",
        "examples_C_AtoT",
        "team:ml",
    ],
)

py_test(
    name = "examples/curriculum_learning",
    size = "medium",
    srcs = ["examples/curriculum_learning.py"],
    args = [
        "--as-test",
        "--stop-reward=800.0",
    ],
    main = "examples/curriculum_learning.py",
    tags = [
        "examples",
        "examples_C",
        "examples_C_UtoZ",
        "team:ml",
    ],
)

py_test(
    name = "examples/custom_env_tf",
    size = "medium",
    srcs = ["examples/custom_env.py"],
    args = ["--as-test"],
    main = "examples/custom_env.py",
    tags = [
        "examples",
        "examples_C",
        "examples_C_UtoZ",
        "team:ml",
    ],
)

py_test(
    name = "examples/custom_env_torch",
    size = "large",
    srcs = ["examples/custom_env.py"],
    args = [
        "--as-test",
        "--framework=torch",
    ],
    main = "examples/custom_env.py",
    tags = [
        "examples",
        "examples_C",
        "examples_C_UtoZ",
        "team:ml",
    ],
)

py_test(
    name = "examples/custom_eval_tf",
    size = "medium",
    srcs = ["examples/custom_eval.py"],
    args = [
        "--num-cpus=4",
        "--as-test",
    ],
    main = "examples/custom_eval.py",
    tags = [
        "examples",
        "examples_C",
        "examples_C_UtoZ",
        "team:ml",
    ],
)

py_test(
    name = "examples/custom_eval_torch",
    size = "medium",
    srcs = ["examples/custom_eval.py"],
    args = [
        "--num-cpus=4",
        "--as-test",
        "--framework=torch",
    ],
    main = "examples/custom_eval.py",
    tags = [
        "examples",
        "examples_C",
        "examples_C_UtoZ",
        "team:ml",
    ],
)

py_test(
    name = "examples/custom_experiment",
    size = "medium",
    srcs = ["examples/custom_experiment.py"],
    args = ["--train-iterations=10"],
    main = "examples/custom_experiment.py",
    tags = [
        "examples",
        "examples_C",
        "examples_C_UtoZ",
        "team:ml",
    ],
)

py_test(
    name = "examples/custom_fast_model_tf",
    size = "medium",
    srcs = ["examples/custom_fast_model.py"],
    args = ["--stop-iters=1"],
    main = "examples/custom_fast_model.py",
    tags = [
        "examples",
        "examples_C",
        "examples_C_UtoZ",
        "team:ml",
    ],
)

py_test(
    name = "examples/custom_fast_model_torch",
    size = "medium",
    srcs = ["examples/custom_fast_model.py"],
    args = [
        "--stop-iters=1",
        "--framework=torch",
    ],
    main = "examples/custom_fast_model.py",
    tags = [
        "examples",
        "examples_C",
        "examples_C_UtoZ",
        "team:ml",
    ],
)

py_test(
    name = "examples/custom_keras_model_a2c",
    size = "large",
    srcs = ["examples/custom_keras_model.py"],
    args = [
        "--run=A2C",
        "--stop=50",
        "--num-cpus=4",
    ],
    main = "examples/custom_keras_model.py",
    tags = [
        "examples",
        "examples_C",
        "examples_C_UtoZ",
        "team:ml",
    ],
)

py_test(
    name = "examples/custom_keras_model_dqn",
    size = "medium",
    srcs = ["examples/custom_keras_model.py"],
    args = [
        "--run=DQN",
        "--stop=50",
    ],
    main = "examples/custom_keras_model.py",
    tags = [
        "examples",
        "examples_C",
        "examples_C_UtoZ",
        "team:ml",
    ],
)

py_test(
    name = "examples/custom_keras_model_ppo",
    size = "medium",
    srcs = ["examples/custom_keras_model.py"],
    args = [
        "--run=PPO",
        "--stop=50",
        "--num-cpus=4",
    ],
    main = "examples/custom_keras_model.py",
    tags = [
        "examples",
        "examples_C",
        "examples_C_UtoZ",
        "team:ml",
    ],
)

py_test(
    name = "examples/custom_metrics_and_callbacks",
    size = "small",
    srcs = ["examples/custom_metrics_and_callbacks.py"],
    args = ["--stop-iters=2"],
    main = "examples/custom_metrics_and_callbacks.py",
    tags = [
        "examples",
        "examples_C",
        "examples_C_UtoZ",
        "team:ml",
    ],
)

py_test(
    name = "examples/custom_metrics_and_callbacks_legacy",
    size = "small",
    srcs = ["examples/custom_metrics_and_callbacks_legacy.py"],
    args = ["--stop-iters=2"],
    main = "examples/custom_metrics_and_callbacks_legacy.py",
    tags = [
        "examples",
        "examples_C",
        "examples_C_UtoZ",
        "team:ml",
    ],
)

py_test(
    name = "examples/custom_model_api_tf",
    size = "small",
    srcs = ["examples/custom_model_api.py"],
    main = "examples/custom_model_api.py",
    tags = [
        "examples",
        "examples_C",
        "examples_C_UtoZ",
        "team:ml",
    ],
)

py_test(
    name = "examples/custom_model_api_torch",
    size = "small",
    srcs = ["examples/custom_model_api.py"],
    args = ["--framework=torch"],
    main = "examples/custom_model_api.py",
    tags = [
        "examples",
        "examples_C",
        "examples_C_UtoZ",
        "team:ml",
    ],
)

py_test(
    name = "examples/custom_model_loss_and_metrics_ppo_tf",
    size = "medium",
    srcs = ["examples/custom_model_loss_and_metrics.py"],
    args = [
        "--run=PPO",
        "--stop-iters=1",
        "--input-files=tests/data/cartpole",
    ],
    # Include the json data file.
    data = ["tests/data/cartpole/small.json"],
    main = "examples/custom_model_loss_and_metrics.py",
    tags = [
        "examples",
        "examples_C",
        "examples_C_UtoZ",
        "team:ml",
    ],
)

py_test(
    name = "examples/custom_model_loss_and_metrics_ppo_torch",
    size = "medium",
    srcs = ["examples/custom_model_loss_and_metrics.py"],
    args = [
        "--run=PPO",
        "--framework=torch",
        "--stop-iters=1",
        "--input-files=tests/data/cartpole",
    ],
    # Include the json data file.
    data = ["tests/data/cartpole/small.json"],
    main = "examples/custom_model_loss_and_metrics.py",
    tags = [
        "examples",
        "examples_C",
        "examples_C_UtoZ",
        "team:ml",
    ],
)

py_test(
    name = "examples/custom_model_loss_and_metrics_pg_tf",
    size = "medium",
    srcs = ["examples/custom_model_loss_and_metrics.py"],
    args = [
        "--run=PG",
        "--stop-iters=1",
        "--input-files=tests/data/cartpole",
    ],
    # Include the json data file.
    data = ["tests/data/cartpole/small.json"],
    main = "examples/custom_model_loss_and_metrics.py",
    tags = [
        "examples",
        "examples_C",
        "examples_C_UtoZ",
        "team:ml",
    ],
)

py_test(
    name = "examples/custom_model_loss_and_metrics_pg_torch",
    size = "medium",
    srcs = ["examples/custom_model_loss_and_metrics.py"],
    args = [
        "--run=PG",
        "--framework=torch",
        "--stop-iters=1",
        "--input-files=tests/data/cartpole",
    ],
    # Include the json data file.
    data = ["tests/data/cartpole/small.json"],
    main = "examples/custom_model_loss_and_metrics.py",
    tags = [
        "examples",
        "examples_C",
        "examples_C_UtoZ",
        "team:ml",
    ],
)

py_test(
    name = "examples/custom_observation_filters",
    size = "medium",
    srcs = ["examples/custom_observation_filters.py"],
    args = ["--stop-iters=3"],
    main = "examples/custom_observation_filters.py",
    tags = [
        "examples",
        "examples_C",
        "examples_C_UtoZ",
        "team:ml",
    ],
)

py_test(
    name = "examples/custom_rnn_model_repeat_after_me_tf",
    size = "medium",
    srcs = ["examples/custom_rnn_model.py"],
    args = [
        "--as-test",
        "--run=PPO",
        "--stop-reward=40",
        "--env=RepeatAfterMeEnv",
        "--num-cpus=4",
    ],
    main = "examples/custom_rnn_model.py",
    tags = [
        "examples",
        "examples_C",
        "examples_C_UtoZ",
        "team:ml",
    ],
)

py_test(
    name = "examples/custom_rnn_model_repeat_initial_obs_tf",
    size = "medium",
    srcs = ["examples/custom_rnn_model.py"],
    args = [
        "--as-test",
        "--run=PPO",
        "--stop-reward=10",
        "--stop-timesteps=300000",
        "--env=RepeatInitialObsEnv",
        "--num-cpus=4",
    ],
    main = "examples/custom_rnn_model.py",
    tags = [
        "examples",
        "examples_C",
        "examples_C_UtoZ",
        "team:ml",
    ],
)

py_test(
    name = "examples/custom_rnn_model_repeat_after_me_torch",
    size = "medium",
    srcs = ["examples/custom_rnn_model.py"],
    args = [
        "--as-test",
        "--framework=torch",
        "--run=PPO",
        "--stop-reward=40",
        "--env=RepeatAfterMeEnv",
        "--num-cpus=4",
    ],
    main = "examples/custom_rnn_model.py",
    tags = [
        "examples",
        "examples_C",
        "examples_C_UtoZ",
        "team:ml",
    ],
)

py_test(
    name = "examples/custom_rnn_model_repeat_initial_obs_torch",
    size = "medium",
    srcs = ["examples/custom_rnn_model.py"],
    args = [
        "--as-test",
        "--framework=torch",
        "--run=PPO",
        "--stop-reward=10",
        "--stop-timesteps=300000",
        "--env=RepeatInitialObsEnv",
        "--num-cpus=4",
    ],
    main = "examples/custom_rnn_model.py",
    tags = [
        "examples",
        "examples_C",
        "examples_C_UtoZ",
        "team:ml",
    ],
)

py_test(
    name = "examples/custom_tf_policy",
    size = "medium",
    srcs = ["examples/custom_tf_policy.py"],
    args = [
        "--stop-iters=2",
        "--num-cpus=4",
    ],
    tags = [
        "examples",
        "examples_C",
        "examples_C_UtoZ",
        "team:ml",
    ],
)

py_test(
    name = "examples/custom_torch_policy",
    size = "medium",
    srcs = ["examples/custom_torch_policy.py"],
    args = [
        "--stop-iters=2",
        "--num-cpus=4",
    ],
    tags = [
        "examples",
        "examples_C",
        "examples_C_UtoZ",
        "team:ml",
    ],
)

py_test(
    name = "examples/custom_train_fn",
    size = "medium",
    srcs = ["examples/custom_train_fn.py"],
    main = "examples/custom_train_fn.py",
    tags = [
        "examples",
        "examples_C",
        "examples_C_UtoZ",
        "team:ml",
    ],
)

py_test(
    name = "examples/custom_vector_env_tf",
    size = "medium",
    srcs = ["examples/custom_vector_env.py"],
    args = [
        "--as-test",
        "--stop-reward=40.0",
    ],
    main = "examples/custom_vector_env.py",
    tags = [
        "examples",
        "examples_C",
        "examples_C_UtoZ",
        "team:ml",
    ],
)

py_test(
    name = "examples/custom_vector_env_torch",
    size = "medium",
    srcs = ["examples/custom_vector_env.py"],
    args = [
        "--as-test",
        "--framework=torch",
        "--stop-reward=40.0",
    ],
    main = "examples/custom_vector_env.py",
    tags = [
        "examples",
        "examples_C",
        "examples_C_UtoZ",
        "team:ml",
    ],
)

py_test(
    name = "examples/deterministic_training_tf",
    size = "medium",
    srcs = ["examples/deterministic_training.py"],
    args = [
        "--as-test",
        "--stop-iters=1",
        "--framework=tf",
        "--num-gpus-trainer=1",
        "--num-gpus-per-worker=1",
    ],
    main = "examples/deterministic_training.py",
    tags = [
        "multi_gpu",
        "team:ml",
    ],
)

py_test(
    name = "examples/deterministic_training_tf2",
    size = "medium",
    srcs = ["examples/deterministic_training.py"],
    args = [
        "--as-test",
        "--stop-iters=1",
        "--framework=tf2",
        "--num-gpus-trainer=1",
        "--num-gpus-per-worker=1",
    ],
    main = "examples/deterministic_training.py",
    tags = [
        "multi_gpu",
        "team:ml",
    ],
)

py_test(
    name = "examples/deterministic_training_torch",
    size = "medium",
    srcs = ["examples/deterministic_training.py"],
    args = [
        "--as-test",
        "--stop-iters=1",
        "--framework=torch",
        "--num-gpus-trainer=1",
        "--num-gpus-per-worker=1",
    ],
    main = "examples/deterministic_training.py",
    tags = [
        "multi_gpu",
        "team:ml",
    ],
)

py_test(
    name = "examples/eager_execution",
    size = "small",
    srcs = ["examples/eager_execution.py"],
    args = ["--stop-iters=2"],
    tags = [
        "examples",
        "examples_E",
        "team:ml",
    ],
)

py_test(
    name = "examples/export/cartpole_dqn_export",
    size = "medium",
    srcs = ["examples/export/cartpole_dqn_export.py"],
    main = "examples/export/cartpole_dqn_export.py",
    tags = [
        "examples",
        "examples_E",
        "team:ml",
    ],
)

py_test(
    name = "examples/export/onnx_tf",
    size = "medium",
    srcs = ["examples/export/onnx_tf.py"],
    main = "examples/export/onnx_tf.py",
    tags = [
        "examples",
        "examples_E",
        "team:ml",
    ],
)

py_test(
    name = "examples/export/onnx_torch",
    size = "medium",
    srcs = ["examples/export/onnx_torch.py"],
    main = "examples/export/onnx_torch.py",
    tags = [
        "examples",
        "examples_E",
        "team:ml",
    ],
)

py_test(
    name = "examples/fractional_gpus",
    size = "medium",
    srcs = ["examples/fractional_gpus.py"],
    args = [
        "--as-test",
        "--stop-reward=40.0",
        "--num-gpus=0",
        "--num-workers=0",
    ],
    main = "examples/fractional_gpus.py",
    tags = [
        "examples",
        "examples_F",
        "team:ml",
    ],
)

py_test(
    name = "examples/hierarchical_training_tf",
    size = "medium",
    srcs = ["examples/hierarchical_training.py"],
    args = ["--stop-reward=0.0"],
    main = "examples/hierarchical_training.py",
    tags = [
        "examples",
        "examples_H",
        "team:ml",
    ],
)

py_test(
    name = "examples/hierarchical_training_torch",
    size = "medium",
    srcs = ["examples/hierarchical_training.py"],
    args = [
        "--framework=torch",
        "--stop-reward=0.0",
    ],
    main = "examples/hierarchical_training.py",
    tags = [
        "examples",
        "examples_H",
        "team:ml",
    ],
)

# Do not run this test (MobileNetV2 is gigantic and takes forever for 1 iter).
# py_test(
#     name = "examples/mobilenet_v2_with_lstm_tf",
#     main = "examples/mobilenet_v2_with_lstm.py",
#     tags = ["team:ml", "examples", "examples_M"],
#     size = "small",
#     srcs = ["examples/mobilenet_v2_with_lstm.py"]
# )

py_test(
    name = "examples/multi_agent_cartpole_tf",
    size = "medium",
    srcs = ["examples/multi_agent_cartpole.py"],
    args = [
        "--as-test",
        "--stop-reward=70.0",
        "--num-cpus=4",
    ],
    main = "examples/multi_agent_cartpole.py",
    tags = [
        "examples",
        "examples_M",
        "team:ml",
    ],
)

py_test(
    name = "examples/multi_agent_cartpole_torch",
    size = "medium",
    srcs = ["examples/multi_agent_cartpole.py"],
    args = [
        "--as-test",
        "--framework=torch",
        "--stop-reward=70.0",
        "--num-cpus=4",
    ],
    main = "examples/multi_agent_cartpole.py",
    tags = [
        "examples",
        "examples_M",
        "team:ml",
    ],
)

py_test(
    name = "examples/multi_agent_custom_policy_tf",
    size = "small",
    srcs = ["examples/multi_agent_custom_policy.py"],
    args = [
        "--as-test",
        "--stop-reward=80",
    ],
    main = "examples/multi_agent_custom_policy.py",
    tags = [
        "examples",
        "examples_M",
        "team:ml",
    ],
)

py_test(
    name = "examples/multi_agent_custom_policy_torch",
    size = "small",
    srcs = ["examples/multi_agent_custom_policy.py"],
    args = [
        "--as-test",
        "--framework=torch",
        "--stop-reward=80",
    ],
    main = "examples/multi_agent_custom_policy.py",
    tags = [
        "examples",
        "examples_M",
        "team:ml",
    ],
)

py_test(
    name = "examples/multi_agent_two_trainers_tf",
    size = "medium",
    srcs = ["examples/multi_agent_two_trainers.py"],
    args = [
        "--as-test",
        "--stop-reward=70",
    ],
    main = "examples/multi_agent_two_trainers.py",
    tags = [
        "examples",
        "examples_M",
        "team:ml",
    ],
)

py_test(
    name = "examples/multi_agent_two_trainers_torch",
    size = "medium",
    srcs = ["examples/multi_agent_two_trainers.py"],
    args = [
        "--as-test",
        "--framework=torch",
        "--stop-reward=70",
    ],
    main = "examples/multi_agent_two_trainers.py",
    tags = [
        "examples",
        "examples_M",
        "team:ml",
    ],
)

# Taking out this test for now: Mixed torch- and tf- policies within the same
# Trainer never really worked.
# py_test(
#     name = "examples/multi_agent_two_trainers_mixed_torch_tf",
#     main = "examples/multi_agent_two_trainers.py",
#     tags = ["team:ml", "examples", "examples_M"],
#     size = "medium",
#     srcs = ["examples/multi_agent_two_trainers.py"],
#     args = ["--as-test", "--mixed-torch-tf", "--stop-reward=70"]
# )

py_test(
    name = "examples/nested_action_spaces_ppo_tf",
    size = "medium",
    srcs = ["examples/nested_action_spaces.py"],
    args = [
        "--as-test",
        "--stop-reward=-600",
        "--run=PPO",
    ],
    main = "examples/nested_action_spaces.py",
    tags = [
        "examples",
        "examples_N",
        "team:ml",
    ],
)

py_test(
    name = "examples/nested_action_spaces_ppo_torch",
    size = "medium",
    srcs = ["examples/nested_action_spaces.py"],
    args = [
        "--as-test",
        "--framework=torch",
        "--stop-reward=-600",
        "--run=PPO",
    ],
    main = "examples/nested_action_spaces.py",
    tags = [
        "examples",
        "examples_N",
        "team:ml",
    ],
)

py_test(
    name = "examples/parallel_evaluation_and_training_13_episodes_tf",
    size = "medium",
    srcs = ["examples/parallel_evaluation_and_training.py"],
    args = [
        "--as-test",
        "--stop-reward=50.0",
        "--num-cpus=6",
        "--evaluation-duration=13",
    ],
    main = "examples/parallel_evaluation_and_training.py",
    tags = [
        "examples",
        "examples_P",
        "team:ml",
    ],
)

py_test(
    name = "examples/parallel_evaluation_and_training_auto_episodes_tf",
    size = "medium",
    srcs = ["examples/parallel_evaluation_and_training.py"],
    args = [
        "--as-test",
        "--stop-reward=50.0",
        "--num-cpus=6",
        "--evaluation-duration=auto",
    ],
    main = "examples/parallel_evaluation_and_training.py",
    tags = [
        "examples",
        "examples_P",
        "team:ml",
    ],
)

py_test(
    name = "examples/parallel_evaluation_and_training_211_ts_tf2",
    size = "medium",
    srcs = ["examples/parallel_evaluation_and_training.py"],
    args = [
        "--as-test",
        "--framework=tf2",
        "--stop-reward=30.0",
        "--num-cpus=6",
        "--evaluation-num-workers=3",
        "--evaluation-duration=211",
        "--evaluation-duration-unit=timesteps",
    ],
    main = "examples/parallel_evaluation_and_training.py",
    tags = [
        "examples",
        "examples_P",
        "team:ml",
    ],
)

py_test(
    name = "examples/parallel_evaluation_and_training_auto_ts_torch",
    size = "medium",
    srcs = ["examples/parallel_evaluation_and_training.py"],
    args = [
        "--as-test",
        "--framework=torch",
        "--stop-reward=30.0",
        "--num-cpus=6",
        "--evaluation-num-workers=3",
        "--evaluation-duration=auto",
        "--evaluation-duration-unit=timesteps",
    ],
    main = "examples/parallel_evaluation_and_training.py",
    tags = [
        "examples",
        "examples_P",
        "team:ml",
    ],
)

py_test(
    name = "examples/parametric_actions_cartpole_pg_tf",
    size = "medium",
    srcs = ["examples/parametric_actions_cartpole.py"],
    args = [
        "--as-test",
        "--stop-reward=60.0",
        "--run=PG",
    ],
    main = "examples/parametric_actions_cartpole.py",
    tags = [
        "examples",
        "examples_P",
        "team:ml",
    ],
)

py_test(
    name = "examples/parametric_actions_cartpole_dqn_tf",
    size = "medium",
    srcs = ["examples/parametric_actions_cartpole.py"],
    args = [
        "--as-test",
        "--stop-reward=60.0",
        "--run=DQN",
    ],
    main = "examples/parametric_actions_cartpole.py",
    tags = [
        "examples",
        "examples_P",
        "team:ml",
    ],
)

py_test(
    name = "examples/parametric_actions_cartpole_pg_torch",
    size = "medium",
    srcs = ["examples/parametric_actions_cartpole.py"],
    args = [
        "--as-test",
        "--framework=torch",
        "--stop-reward=60.0",
        "--run=PG",
    ],
    main = "examples/parametric_actions_cartpole.py",
    tags = [
        "examples",
        "examples_P",
        "team:ml",
    ],
)

py_test(
    name = "examples/parametric_actions_cartpole_dqn_torch",
    size = "medium",
    srcs = ["examples/parametric_actions_cartpole.py"],
    args = [
        "--as-test",
        "--framework=torch",
        "--stop-reward=60.0",
        "--run=DQN",
    ],
    main = "examples/parametric_actions_cartpole.py",
    tags = [
        "examples",
        "examples_P",
        "team:ml",
    ],
)

py_test(
    name = "examples/parametric_actions_cartpole_embeddings_learnt_by_model",
    size = "medium",
    srcs = ["examples/parametric_actions_cartpole_embeddings_learnt_by_model.py"],
    args = [
        "--as-test",
        "--stop-reward=80.0",
    ],
    main = "examples/parametric_actions_cartpole_embeddings_learnt_by_model.py",
    tags = [
        "examples",
        "examples_P",
        "team:ml",
    ],
)

py_test(
    name = "examples/inference_and_serving/policy_inference_after_training_tf",
    size = "medium",
    srcs = ["examples/inference_and_serving/policy_inference_after_training.py"],
    args = [
        "--stop-iters=3",
        "--framework=tf",
    ],
    main = "examples/inference_and_serving/policy_inference_after_training.py",
    tags = [
        "examples",
        "examples_P",
        "team:ml",
    ],
)

py_test(
    name = "examples/inference_and_serving/policy_inference_after_training_torch",
    size = "medium",
    srcs = ["examples/inference_and_serving/policy_inference_after_training.py"],
    args = [
        "--stop-iters=3",
        "--framework=torch",
    ],
    main = "examples/inference_and_serving/policy_inference_after_training.py",
    tags = [
        "examples",
        "examples_P",
        "team:ml",
    ],
)

py_test(
    name = "examples/inference_and_serving/policy_inference_after_training_with_attention_tf",
    size = "medium",
    srcs = ["examples/inference_and_serving/policy_inference_after_training_with_attention.py"],
    args = [
        "--stop-iters=2",
        "--framework=tf",
    ],
    main = "examples/inference_and_serving/policy_inference_after_training_with_attention.py",
    tags = [
        "examples",
        "examples_P",
        "team:ml",
    ],
)

py_test(
    name = "examples/inference_and_serving/policy_inference_after_training_with_attention_torch",
    size = "medium",
    srcs = ["examples/inference_and_serving/policy_inference_after_training_with_attention.py"],
    args = [
        "--stop-iters=2",
        "--framework=torch",
    ],
    main = "examples/inference_and_serving/policy_inference_after_training_with_attention.py",
    tags = [
        "examples",
        "examples_P",
        "team:ml",
    ],
)

py_test(
    name = "examples/inference_and_serving/policy_inference_after_training_with_lstm_tf",
    size = "medium",
    srcs = ["examples/inference_and_serving/policy_inference_after_training_with_lstm.py"],
    args = [
        "--stop-iters=1",
        "--framework=tf",
    ],
    main = "examples/inference_and_serving/policy_inference_after_training_with_lstm.py",
    tags = [
        "examples",
        "examples_P",
        "team:ml",
    ],
)

py_test(
    name = "examples/inference_and_serving/policy_inference_after_training_with_lstm_torch",
    size = "medium",
    srcs = ["examples/inference_and_serving/policy_inference_after_training_with_lstm.py"],
    args = [
        "--stop-iters=1",
        "--framework=torch",
    ],
    main = "examples/inference_and_serving/policy_inference_after_training_with_lstm.py",
    tags = [
        "examples",
        "examples_P",
        "team:ml",
    ],
)

py_test(
    name = "examples/preprocessing_disabled_tf",
    size = "medium",
    srcs = ["examples/preprocessing_disabled.py"],
    args = ["--stop-iters=2"],
    main = "examples/preprocessing_disabled.py",
    tags = [
        "examples",
        "examples_P",
        "team:ml",
    ],
)

py_test(
    name = "examples/preprocessing_disabled_torch",
    size = "medium",
    srcs = ["examples/preprocessing_disabled.py"],
    args = [
        "--framework=torch",
        "--stop-iters=2",
    ],
    main = "examples/preprocessing_disabled.py",
    tags = [
        "examples",
        "examples_P",
        "team:ml",
    ],
)

py_test(
    name = "examples/recommender_system_with_recsim_and_slateq_tf2",
    size = "large",
    srcs = ["examples/recommender_system_with_recsim_and_slateq.py"],
    args = [
        "--stop-iters=2",
        "--learning-starts=100",
        "--framework=tf2",
        "--use-tune",
        "--random-test-episodes=10",
        "--env-num-candidates=50",
        "--env-slate-size=2",
    ],
    main = "examples/recommender_system_with_recsim_and_slateq.py",
    tags = [
        "examples",
        "examples_R",
        "team:ml",
    ],
)

py_test(
    name = "examples/remote_envs_with_inference_done_on_main_node_tf",
    size = "medium",
    srcs = ["examples/remote_envs_with_inference_done_on_main_node.py"],
    args = ["--as-test"],
    main = "examples/remote_envs_with_inference_done_on_main_node.py",
    tags = [
        "examples",
        "examples_R",
        "team:ml",
    ],
)

py_test(
    name = "examples/remote_envs_with_inference_done_on_main_node_torch",
    size = "medium",
    srcs = ["examples/remote_envs_with_inference_done_on_main_node.py"],
    args = [
        "--as-test",
        "--framework=torch",
    ],
    main = "examples/remote_envs_with_inference_done_on_main_node.py",
    tags = [
        "examples",
        "examples_R",
        "team:ml",
    ],
)

py_test(
    name = "examples/remote_base_env_with_custom_api",
    size = "medium",
    srcs = ["examples/remote_base_env_with_custom_api.py"],
    args = ["--stop-iters=3"],
    tags = [
        "examples",
        "examples_R",
        "team:ml",
    ],
)

py_test(
    name = "examples/restore_1_of_n_agents_from_checkpoint",
    size = "medium",
    srcs = ["examples/restore_1_of_n_agents_from_checkpoint.py"],
    args = [
        "--pre-training-iters=1",
        "--stop-iters=1",
        "--num-cpus=4",
    ],
    tags = [
        "examples",
        "examples_R",
        "team:ml",
    ],
)

py_test(
    name = "examples/rnnsac_stateless_cartpole",
    size = "large",
    srcs = ["examples/rnnsac_stateless_cartpole.py"],
    tags = [
        "gpu",
        "team:ml",
    ],
)

py_test(
    name = "examples/rollout_worker_custom_workflow",
    size = "small",
    srcs = ["examples/rollout_worker_custom_workflow.py"],
    args = ["--num-cpus=4"],
    tags = [
        "examples",
        "examples_R",
        "team:ml",
    ],
)

py_test(
    name = "examples/rock_paper_scissors_multiagent_tf",
    size = "medium",
    srcs = ["examples/rock_paper_scissors_multiagent.py"],
    args = ["--as-test"],
    main = "examples/rock_paper_scissors_multiagent.py",
    tags = [
        "examples",
        "examples_R",
        "team:ml",
    ],
)

py_test(
    name = "examples/rock_paper_scissors_multiagent_torch",
    size = "medium",
    srcs = ["examples/rock_paper_scissors_multiagent.py"],
    args = [
        "--as-test",
        "--framework=torch",
    ],
    main = "examples/rock_paper_scissors_multiagent.py",
    tags = [
        "examples",
        "examples_R",
        "team:ml",
    ],
)

py_test(
    name = "examples/self_play_with_open_spiel_connect_4_tf",
    size = "medium",
    srcs = ["examples/self_play_with_open_spiel.py"],
    args = [
        "--framework=tf",
        "--env=connect_four",
        "--win-rate-threshold=0.6",
        "--stop-iters=2",
        "--num-episodes-human-play=0",
    ],
    main = "examples/self_play_with_open_spiel.py",
    tags = [
        "examples",
        "examples_S",
        "team:ml",
    ],
)

py_test(
    name = "examples/self_play_with_open_spiel_connect_4_torch",
    size = "medium",
    srcs = ["examples/self_play_with_open_spiel.py"],
    args = [
        "--framework=torch",
        "--env=connect_four",
        "--win-rate-threshold=0.6",
        "--stop-iters=2",
        "--num-episodes-human-play=0",
    ],
    main = "examples/self_play_with_open_spiel.py",
    tags = [
        "examples",
        "examples_S",
        "team:ml",
    ],
)

py_test(
    name = "examples/self_play_league_based_with_open_spiel_markov_soccer_tf",
    size = "medium",
    srcs = ["examples/self_play_league_based_with_open_spiel.py"],
    args = [
        "--framework=tf",
        "--env=markov_soccer",
        "--win-rate-threshold=0.6",
        "--stop-iters=2",
        "--num-episodes-human-play=0",
    ],
    main = "examples/self_play_league_based_with_open_spiel.py",
    tags = [
        "examples",
        "examples_S",
        "team:ml",
    ],
)

py_test(
    name = "examples/self_play_league_based_with_open_spiel_markov_soccer_torch",
    size = "medium",
    srcs = ["examples/self_play_league_based_with_open_spiel.py"],
    args = [
        "--framework=torch",
        "--env=markov_soccer",
        "--win-rate-threshold=0.6",
        "--stop-iters=2",
        "--num-episodes-human-play=0",
    ],
    main = "examples/self_play_league_based_with_open_spiel.py",
    tags = [
        "examples",
        "examples_S",
        "team:ml",
    ],
)

py_test(
    name = "examples/trajectory_view_api_tf",
    size = "medium",
    srcs = ["examples/trajectory_view_api.py"],
    args = [
        "--as-test",
        "--framework=tf",
        "--stop-reward=100.0",
    ],
    main = "examples/trajectory_view_api.py",
    tags = [
        "examples",
        "examples_T",
        "team:ml",
    ],
)

py_test(
    name = "examples/trajectory_view_api_torch",
    size = "medium",
    srcs = ["examples/trajectory_view_api.py"],
    args = [
        "--as-test",
        "--framework=torch",
        "--stop-reward=100.0",
    ],
    main = "examples/trajectory_view_api.py",
    tags = [
        "examples",
        "examples_T",
        "team:ml",
    ],
)

py_test(
    name = "examples/tune/framework",
    size = "medium",
    srcs = ["examples/tune/framework.py"],
    args = ["--smoke-test"],
    main = "examples/tune/framework.py",
    tags = [
        "examples",
        "examples_F",
        "team:ml",
    ],
)

py_test(
    name = "examples/two_trainer_workflow_tf",
    size = "medium",
    srcs = ["examples/two_trainer_workflow.py"],
    args = [
        "--as-test",
        "--stop-reward=450.0",
    ],
    main = "examples/two_trainer_workflow.py",
    tags = [
        "examples",
        "examples_T",
        "team:ml",
    ],
)

py_test(
    name = "examples/two_trainer_workflow_torch",
    size = "medium",
    srcs = ["examples/two_trainer_workflow.py"],
    args = [
        "--as-test",
        "--torch",
        "--stop-reward=450.0",
    ],
    main = "examples/two_trainer_workflow.py",
    tags = [
        "examples",
        "examples_T",
        "team:ml",
    ],
)

py_test(
    name = "examples/two_trainer_workflow_mixed_torch_tf",
    size = "medium",
    srcs = ["examples/two_trainer_workflow.py"],
    args = [
        "--as-test",
        "--mixed-torch-tf",
        "--stop-reward=450.0",
    ],
    main = "examples/two_trainer_workflow.py",
    tags = [
        "examples",
        "examples_T",
        "team:ml",
    ],
)

py_test(
    name = "examples/two_step_game_maddpg",
    size = "medium",
    srcs = ["examples/two_step_game.py"],
    args = [
        "--as-test",
        "--stop-reward=7.1",
        "--run=contrib/MADDPG",
    ],
    main = "examples/two_step_game.py",
    tags = [
        "examples",
        "examples_T",
        "team:ml",
    ],
)

py_test(
    name = "examples/two_step_game_pg_tf",
    size = "medium",
    srcs = ["examples/two_step_game.py"],
    args = [
        "--as-test",
        "--stop-reward=7",
        "--run=PG",
    ],
    main = "examples/two_step_game.py",
    tags = [
        "examples",
        "examples_T",
        "team:ml",
    ],
)

py_test(
    name = "examples/two_step_game_pg_torch",
    size = "medium",
    srcs = ["examples/two_step_game.py"],
    args = [
        "--as-test",
        "--framework=torch",
        "--stop-reward=7",
        "--run=PG",
    ],
    main = "examples/two_step_game.py",
    tags = [
        "examples",
        "examples_T",
        "team:ml",
    ],
)

py_test(
    name = "examples/bandit/lin_ts_train_wheel_env",
    size = "small",
    srcs = ["examples/bandit/lin_ts_train_wheel_env.py"],
    main = "examples/bandit/lin_ts_train_wheel_env.py",
    tags = [
        "examples",
        "team:ml",
    ],
)

py_test(
    name = "examples/bandit/tune_lin_ts_train_wheel_env",
    size = "small",
    srcs = ["examples/bandit/tune_lin_ts_train_wheel_env.py"],
    main = "examples/bandit/tune_lin_ts_train_wheel_env.py",
    tags = [
        "examples",
        "team:ml",
    ],
)

py_test(
    name = "examples/bandit/tune_lin_ucb_train_recommendation",
    size = "small",
    srcs = ["examples/bandit/tune_lin_ucb_train_recommendation.py"],
    main = "examples/bandit/tune_lin_ucb_train_recommendation.py",
    tags = [
        "examples",
        "team:ml",
    ],
)

py_test(
    name = "examples/bandit/tune_lin_ucb_train_recsim_env",
    size = "small",
    srcs = ["examples/bandit/tune_lin_ucb_train_recsim_env.py"],
    main = "examples/bandit/tune_lin_ucb_train_recsim_env.py",
    tags = [
        "examples",
        "team:ml",
    ],
)

# --------------------------------------------------------------------
# examples/documentation directory
#
# Tag: documentation
#
# NOTE: Add tests alphabetically to this list.
# --------------------------------------------------------------------

py_test(
    name = "examples/documentation/custom_gym_env",
    size = "medium",
    srcs = ["examples/documentation/custom_gym_env.py"],
    main = "examples/documentation/custom_gym_env.py",
    tags = [
        "documentation",
        "team:ml",
    ],
)

py_test(
    name = "examples/documentation/rllib_in_60s",
    size = "medium",
    srcs = ["examples/documentation/rllib_in_60s.py"],
    main = "examples/documentation/rllib_in_60s.py",
    tags = [
        "documentation",
        "team:ml",
    ],
)

py_test(
    name = "examples/documentation/rllib_on_ray_readme",
    size = "medium",
    srcs = ["examples/documentation/rllib_on_ray_readme.py"],
    main = "examples/documentation/rllib_on_ray_readme.py",
    tags = [
        "documentation",
        "team:ml",
    ],
)

py_test(
    name = "examples/documentation/rllib_on_rllib_readme",
    size = "medium",
    srcs = ["examples/documentation/rllib_on_rllib_readme.py"],
    main = "examples/documentation/rllib_on_rllib_readme.py",
    tags = [
        "documentation",
        "team:ml",
    ],
)

# --------------------------------------------------------------------
# Manual/disabled tests
# --------------------------------------------------------------------
py_test_module_list(
    size = "large",
    extra_srcs = [],
    files = [
        "env/tests/test_multi_agent_env.py",
        "env/wrappers/tests/test_kaggle_wrapper.py",
        "examples/env/tests/test_coin_game_non_vectorized_env.py",
        "examples/env/tests/test_coin_game_vectorized_env.py",
        "examples/env/tests/test_matrix_sequential_social_dilemma.py",
        "examples/env/tests/test_wrappers.py",
        "execution/tests/test_mixin_multi_agent_replay_buffer.py",
        "tests/test_dnc.py",
        "tests/test_perf.py",
        "tests/test_vector_env.py",
        "utils/tests/test_check_env.py",
        "utils/tests/test_check_multi_agent.py",
        "utils/tests/test_errors.py",
        "utils/tests/test_utils.py",
    ],
    tags = [
        "manual",
        "team:ml",
    ],
    deps = [],
)
