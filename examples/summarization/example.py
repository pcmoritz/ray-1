import numpy as np

from gym.envs.registration import register
import ray.rllib.ppo as ppo

register(id='SimpleSummarization-v0', entry_point='summarization:SummarizationEnv', kwargs={}, nondeterministic=False)

alg = ppo.PPOAgent("SimpleSummarization-v0")

for i in range(100):
    result = alg.train()
    print("current status: {}".format(result))
