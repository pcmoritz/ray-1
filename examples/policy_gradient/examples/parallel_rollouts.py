from reinforce.policy import ProximalPolicyLoss
from reinforce.env import NoPreprocessor, AtariRamPreprocessor, AtariPixelPreprocessor
import numpy as np
from reinforce.env import BatchedEnv
import tensorflow as tf
import os
import time

import ray
ray.init(num_workers=64, num_cpus=64)

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

# sess = tf.Session(config=tf.ConfigProto(intra_op_parallelism_threads=1))

sess = tf.Session()

ppo = ProximalPolicyLoss(env.observation_space, env.action_space, preprocessor, config, sess)

sess.run(tf.global_variables_initializer())

observation = preprocessor(env.reset())
ppo.compute_actions(observation)
# 100 loops, best of 3: 2.77 ms per loop

## Torch network

import torch.nn as nn
import torch.autograd as autograd
import torch.nn.functional as F
import torch

class VisionNet(nn.Module):
  def __init__(self, num_classes=6):
    super(VisionNet, self).__init__()
    self.features = nn.Sequential(
      nn.Conv2d(3, 16, kernel_size=8, stride=4),
      nn.ReLU(inplace=True),
      nn.Conv2d(16, 32, kernel_size=4, stride=2),
      nn.ReLU(inplace=True),
    )
    self.classifier = nn.Sequential(
      nn.Linear(32 * 8 * 8, 512),
      nn.ReLU(inplace=True),
      nn.Linear(512, num_classes),
    )

  def forward(self, x):
    x = self.features(x)
    x = x.view(x.size(0), 32 * 8 * 8)
    x = self.classifier(x)
    return x

obs = observation.transpose(0, 3, 2, 1)
net = VisionNet().float().cuda(0)

def eval_net(data):
  tensor = torch.from_numpy(data).type(torch.FloatTensor).cuda(0)
  return F.softmax(net.forward(autograd.Variable(tensor))).multinomial().cpu().data.numpy()

## Everything on the cpu (no batching):

@ray.actor
class Agent(object):
  def __init__(self):
    self.env = gym.make("Pong-v0")
    os.environ["CUDA_VISIBLE_DEVICES"] = ""
    sess = tf.Session()
    config = {"kl_coeff": 0.2,
          "num_sgd_iter": 30,
          "sgd_stepsize": 5e-5,
          "sgd_batchsize": 128,
          "entropy_coeff": 0.0,
          "clip_param": 0.3,
          "kl_target": 0.01,
          "timesteps_per_batch": 5000}
    self.preprocessor = AtariPixelPreprocessor()
    self.ppo = ProximalPolicyLoss(self.env.observation_space, self.env.action_space, self.preprocessor, config, sess)
    sess.run(tf.global_variables_initializer())
  def rollout(self):
    observation = self.preprocessor(self.env.reset())
    for i in range(1000):
      action, logprobs = self.ppo.compute_actions(observation)
      for skip in range(6):
        observation, reward, done, info = self.env.step(action)
        if done:
          observation = self.preprocessor(self.env.reset())
        else:
          observation = self.preprocessor(observation)

actors = []
for i in range(64):
  time.sleep(0.5)
  actors.append(Agent())

ray.get([actors[i].rollout() for i in range(64)])

## Batched for gpu (rollouts not parallel)

env = BatchedEnv("Pong-v0", 64, preprocessor)

def rollout(env):
  observation = env.reset()
  for i in range(1000):
    action, logprobs = ppo.compute_actions(observation)
    for skip in range(6):
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
        for i in range(6):
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

# TensorFlow

env = ParallelEnv("Pong-v0", 64, preprocessor)

def rollout(env):
  observation = env.reset()
  for i in range(1000):
    action, logprobs = ppo.compute_actions(observation)
    # action = 64 * [0]
    observation = env.step(64 * [0])

# Torch

def rollout(env):
  observation = env.reset()
  for i in range(1000):
    # action = eval_net(observation.transpose(0, 3, 2, 1))
    # action = 64 * [0]
    observation = env.step(action)
