import ray
from ray.tune.registry import get_registry, register_env
from ray.rllib import ppo
import gym
import retro
import numpy as np

class StochasticFrameSkip(gym.Wrapper):
    def __init__(self, env, n, stickprob):
        gym.Wrapper.__init__(self, env)
        self.n = n
        self.stickprob = stickprob
        self.curac = None
        self.rng = np.random.RandomState()

    def reset(self, **kwargs):
        self.curac = None
        return self.env.reset(**kwargs)

    def step(self, ac):
        done = False
        totrew = 0
        for i in range(self.n):
            # First step after reset, use action
            if self.curac is None:
                self.curac = ac
            # First substep, delay with probability=stickprob
            elif i == 0:
                if self.rng.rand() > self.stickprob:
                    self.curac = ac
            # Second substep, new action definitely kicks in
            elif i == 1:
                self.curac = ac
            ob, rew, done, info = self.env.step(self.curac)
            totrew += rew
            if done:
                break
        return ob, totrew, done, info

def make(game, state, discrete_actions=False):
    use_restricted_actions = retro.ACTIONS_FILTERED
    if discrete_actions:
        use_restricted_actions = retro.ACTIONS_DISCRETE
    env = retro.make(game, state, scenario='contest', use_restricted_actions=use_restricted_actions)
    env = StochasticFrameSkip(env, n=4, stickprob=0.25)
    env = gym.wrappers.TimeLimit(env, max_episode_steps=4500)
    return env

env_name = "sonic_env"
register_env(env_name, lambda config: make(game='SonicTheHedgehog-Genesis', state='LabyrinthZone.Act1'))

ray.init()

config = ppo.DEFAULT_CONFIG.copy()

config.update({
  "timesteps_per_batch": 10000,
  "min_steps_per_task": 100,
  "num_workers": 16,
  "lambda": 0.95,
  "clip_param": 0.2,
  "num_sgd_iter": 20,
  "sgd_batchsize": 4096,
  "use_gae": False,
  "devices": ["/gpu:0"],
  "tf_session_args": {
    "gpu_options": {"allow_growth": True}
  }
})

alg = ppo.PPOAgent(config=config, env=env_name, registry=get_registry())

for i in range(100):
    result = alg.train()
    print("result = {}".format(result))
