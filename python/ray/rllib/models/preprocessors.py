from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import gensim


class Preprocessor(object):
    """Defines an abstract observation preprocessor function."""

    def __init__(self, options):
        self.options = options
        self._init()

    def _init(self):
        pass

    def transform_shape(self, obs_shape):
        """Returns the preprocessed observation shape."""
        raise NotImplementedError

    def transform(self, observation):
        """Returns the preprocessed observation."""
        raise NotImplementedError


class AtariPixelPreprocessor(Preprocessor):
    def _init(self):
        self.downscale_factor = self.options.get("downscale_factor", 2)
        self.dim = int(160 / self.downscale_factor)

    def transform_shape(self, obs_shape):
        return (self.dim, self.dim, 3)

    # TODO(ekl) why does this need to return an extra size-1 dim (the [None])
    def transform(self, observation):
        """Downsamples images from (210, 160, 3) by the configured factor."""
        scaled = observation[
            25:-25:self.downscale_factor, ::self.downscale_factor, :][None]
        return (scaled - 128) / 128


class AtariRamPreprocessor(Preprocessor):
    def transform_shape(self, obs_shape):
        return (128,)

    def transform(self, observation):
        return (observation - 128) / 128


class NoPreprocessor(Preprocessor):
    def transform_shape(self, obs_shape):
        return obs_shape

    def transform(self, observation):
        return observation

model = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)

class Word2VecPreprocessor(Preprocessor):
    def transform_shape(self, obs_shape):
        return (4, 300)

    def transform(self, observation):
        past, future = observation
        return np.concatenate([model.wv[word] for word in past + future])
