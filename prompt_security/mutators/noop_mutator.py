
import random
import math
import string
from prompt_security.mutators.base import PromptMutator


class NoopPromptMutator(PromptMutator):
  def __init__(self,):
      pass

  def mutate(self,sample:str)->str:
      return sample

  def get_name(self):
      return 'noop'
