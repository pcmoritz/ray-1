import numpy as np

from gym.envs.registration import register
import ray.rllib.ppo as ppo

register(id='SimpleSummarization-v0', entry_point='summarization:SummarizationEnv', kwargs={"filepath": "/mnt/data/news_summary.csv"}, nondeterministic=False)

config = ppo.DEFAULT_CONFIG.copy()
alg = ppo.PPOAgent("SimpleSummarization-v0", config)

for i in range(100):
    result = alg.train()
    print("current status: {}".format(result))
