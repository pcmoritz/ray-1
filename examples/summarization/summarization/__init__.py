from .summarization import SummarizationEnv

from gym.envs.registration import register

register(id='SimpleSummarization-v0', entry_point='summarization:SummarizationEnv', kwargs={"filepath": "/mnt/data/wikipedia-summaries.csv"}, nondeterministic=False)

