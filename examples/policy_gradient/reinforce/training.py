# Code for fitting the PPO object on multiple gpus

def train():
  tower_grads = []
  with tf.variable_scope(tf.get_variable_scope()):
    with tf.device('/gpu:%d' % i):
      with tf.name_scope('%s_%d' % ("pi", i)) as scope:

class PPOTrainer(object):
  def __init__(self, observation_space, action_space, preprocessor, config):
    
    self.ppo = ProximalPolicyLoss(observation_space, action_space, preprocessor, config, None)

  def run(self):
    
