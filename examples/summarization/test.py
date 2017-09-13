import gym
import numpy as np

import ray
import ray.rllib.ppo as ppo
import summarization

ray.init()

config = ppo.DEFAULT_CONFIG.copy()
alg = ppo.PPOAgent("SimpleSummarization-v0", config)

env = gym.make("SimpleSummarization-v0")

text = []
summary = []

obs = env.reset()
for i in range(100):
    print("obs", obs)
    action = alg.compute_action(alg.model.preprocessor.transform(obs))
    text.append(obs[1][0])
    if action == 1:
        summary.append(obs[1][0])
    print("text", text)
    print("summary", summary)
    print("action", action)
    obs, reward, done, info = env.step(action)
