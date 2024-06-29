
import random
import math
import string
from prompt_security.mutators.base import PromptMutator


class TypoPromptMutator(PromptMutator):
  def __init__(self,percentage=0.05):
    self.percentage=percentage

  def mutate(self,sample:str)->str:
      return self.__add_typos_to_text(sample,self.percentage)

  def get_name(self):
      return f'TypoPromptMutator-{self.percentage}'

  def __introduce_typos(self,word):
      char_list = list(word)
      i = random.randint(0, len(char_list) - 1)
      char_list[i] = random.choice(string.ascii_lowercase)
      return ''.join(char_list)

  def __add_typos_to_text(self,text,  change_percentage=0.05):
      words = text.split()
      num_words = len(words)
      num_changes = math.ceil(num_words * change_percentage)
      words_to_change = random.sample(words, min(num_changes, num_words))
      for i, word in enumerate(words):
          if word in words_to_change:
              words[i] = self.__introduce_typos(word)

      return ' '.join(words)
