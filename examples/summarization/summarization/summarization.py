from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import collections
import csv
import gym
import gym.spaces
import random
import sys
from spacy.en import English

from .rouge import Rouge

Datapoint = collections.namedtuple('Datapoint', ['text', 'summary'])

class WordSequencePair(gym.Space):
    def __init__(self, past_context_size, future_context_size):
        self.shape = (8 * 300,)
        self.past_context_size = past_context_size
        self.future_context_size = future_context_size

class SummarizationEnv(gym.Env):

    def __init__(self, filepath):
        self.action_space = gym.spaces.Discrete(2)
        # Word2Vec of the last two words in the text and the last two
        # words in the summary
        self.observation_space = WordSequencePair(4, 4)
        self.scorer = Rouge()
        self.data = []
        nlp = English()
        csv.field_size_limit(sys.maxsize)
        with open(filepath) as f:
            reader = csv.reader(f, delimiter=",", quotechar="|", quoting=csv.QUOTE_MINIMAL)
            for row in reader:
                doc1 = nlp(row[0])
                sentences1 = [sent.string.strip() for sent in doc1.sents]
                doc2 = nlp(row[1])
                sentences2 = [sent.string.strip() for sent in doc2.sents]
                self.data.append(Datapoint(text=sentences1, summary=sentences2))
        self.reset()

    def reset(self):
        from datetime import datetime
        random.seed(datetime.now())
        self.current_document = random.randint(1, len(self.data)-1)
        self.current_token = 0
        self.prediction_so_far = []
        self.last_score = 0.0
        self.done = False
        return (self.observation_space.past_context_size * [""], self.observation_space.future_context_size * [""])

    def step(self, action):
        text = self.data[self.current_document].text
        summary = self.data[self.current_document].summary
        if action == 1:
            self.prediction_so_far.append(text[self.current_token])
        if self.done:
            return (self.observation_space.past_context_size * [""], self.observation_space.future_context_size * [""]), 0.0, self.done, {}
        self.current_token += 1
        score = self.scorer.calculate_score(summary, self.prediction_so_far)
        reward = score - self.last_score
        self.last_score = score
        self.done = self.current_token == len(self.data[self.current_document].summary) or self.current_token >= len(text) - 1
        p = self.observation_space.past_context_size
        f = self.observation_space.future_context_size
        past = (p * [""] + text[:self.current_token])[-p:]
        future = (text[self.current_token:] + f * [""])[0:f]
        return (past, future), reward, self.done, {}
