import numpy as np

import ray
import ray.rllib.ppo as ppo
import summarization

ray.init()

@ray.remote
def import_summarization():
    summarization

config = ppo.DEFAULT_CONFIG.copy()
alg = ppo.PPOAgent("SimpleSummarization-v0", config)

for i in range(100):
    result = alg.train()
    print("current status: {}".format(result))
