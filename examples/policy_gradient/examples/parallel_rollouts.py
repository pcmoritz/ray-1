from reinforce.policy import ProximalPolicyLoss
from reinforce.env import NoPreprocessor, AtariRamPreprocessor, AtariPixelPreprocessor
import numpy as np
import tensorflow as tf
from reinforce.env import BatchedEnv

import gym

config = {"kl_coeff": 0.2,
          "num_sgd_iter": 30,
          "sgd_stepsize": 5e-5,
          "sgd_batchsize": 128,
          "entropy_coeff": 0.0,
          "clip_param": 0.3,
          "kl_target": 0.01,
          "timesteps_per_batch": 5000}

preprocessor = AtariPixelPreprocessor()
env = gym.make("Pong-v0")

sess = tf.Session(config=tf.ConfigProto(intra_op_parallelism_threads=1))

ppo = ProximalPolicyLoss(env.observation_space, env.action_space, preprocessor, config, sess)

sess.run(tf.global_variables_initializer())

observation = preprocessor(env.reset())
ppo.compute_actions(observation)

## Everything on the cpu (no batching):

env = gym.make("Pong-v0")

def rollout(env):
  observation = preprocessor(env.reset())
  for i in range(1000):
    action, logprobs = ppo.compute_actions(observation)
    for skip in range(1):
      observation, reward, done, info = env.step(action)
      if done:
        observation = preprocessor(env.reset())
      else:
        observation = preprocessor(observation)

## Batched for gpu (rollouts not parallel)

env = BatchedEnv("Pong-v0", 64, preprocessor)

def rollout(env):
  observation = env.reset()
  for i in range(1000):
    action, logprobs = ppo.compute_actions(observation)
    for skip in range(1):
      observation, reward, done = env.step(action)
      if done.any(): observation = env.reset()

## Everything batched and parallel

class ParallelEnv(object):

  def __init__(self, mdp_name, batch_size, preprocessor):

    @ray.actor
    class Environment(object):
      def __init__(self):
        self.env = gym.make(mdp_name)
        self.env.reset()
      def step(self, action):
        observation, reward, done, info = self.env.step(action)
        if done: observation = self.env.reset()
        return preprocessor(observation)
      def reset(self):
        return preprocessor(self.env.reset())

    self.envs = [Environment() for i in range(batch_size)]

  def step(self, actions):
    return np.concatenate(ray.get([self.envs[i].step(actions[i]) for i in range(len(self.envs))]))

  def reset(self):
    return np.concatenate(ray.get([env.reset() for env in self.envs]))

env = ParallelEnv("Pong-v0", 64, preprocessor)

def rollout(env):
  observation = env.reset()
  for i in range(1000):
    action, logprobs = ppo.compute_actions(observation)
    observation = env.step(action)
