import gym
import numpy as np

import ray
import ray.rllib.ppo as ppo
import summarization

ray.init()

config = ppo.DEFAULT_CONFIG.copy()
alg = ppo.PPOAgent("SimpleSummarization-v0", config)

env = gym.make("SimpleSummarization-v0")


alg.compute_action(alg.model.preprocessor.transform(obs))
