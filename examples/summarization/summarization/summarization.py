from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import collections
import csv
import gym
import gym.spaces
import random

from .rouge import Rouge

Datapoint = collections.namedtuple('Datapoint', ['text', 'summary'])

class WordSequencePair(gym.Space):
    def __init__(self, past_context_size, future_context_size):
        self.shape = (4 * 300,)
        self.past_context_size = past_context_size
        self.future_context_size = future_context_size

class SummarizationEnv(gym.Env):

    def __init__(self, filepath):
        self.action_space = gym.spaces.Discrete(2)
        # Word2Vec of the last two words in the text and the last two
        # words in the summary
        self.observation_space = WordSequencePair(2, 2)
        self.scorer = Rouge()
        self.data = []
        with open(filepath, encoding='iso-8859-1') as f:
            news_reader = csv.reader(f, delimiter=",")
            for row in news_reader:
                 text = row[4].split(" ")
                 summary = row[5].split(" ")
                 self.data.append(Datapoint(text=text, summary=summary))
        self.reset()

    def reset(self):
        self.current_document = random.randint(1, len(self.data))
        self.current_token = 0
        self.prediction_so_far = []
        self.last_score = 0.0
        self.done = False
        return (self.observation_space.past_context_size * [""], self.observation_space.future_context_size * [""])

    def step(self, action):
        text = self.data[self.current_document].text
        if action == 1:
            self.prediction_so_far.append(text[self.current_token])
        if self.done:
            return (self.observation_space.past_context_size * [""], self.observation_space.future_context_size * [""]), 0.0, self.done, {}
        self.current_token += 1
        score = self.scorer.calculate_score(text, self.prediction_so_far)
        reward = score - self.last_score
        self.last_score = reward
        self.done = self.current_token == len(self.data[self.current_document].summary) or self.current_token >= len(text) - 1
        p = self.observation_space.past_context_size
        f = self.observation_space.future_context_size
        past = (p * [""] + text[:self.current_token])[-p:]
        future = (text[self.current_token:] + f * [""])[0:f]
        return (past, future), reward, self.done, {}
