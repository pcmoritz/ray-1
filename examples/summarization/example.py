import gensim
import numpy as np

from gym.envs.registration import register

register(id='SimpleSummarization-v0', entry_point='summarization:SummarizationEnv', kwargs={}, nondeterministic=False)

from ray.rllib.models.preprocessor import Preprocessor

model = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)

class Word2VecPreprocessor(Preprocessor):
    def transform_shape(self, obs_shape):
        return (4, 300)

    def transform(self, observation):
        past, future = observation
        return np.concatenate([model.wv[word] for word in past + future])

alg = pg.PolicyGradient("SimpleSummarization-v0")

for i in range(100):
    result = alg.train()
    print("current status: {}".format(result))
