# Python program showing
# abstract base class work
from abc import ABC, abstractmethod
from typing import List

class PromptMutator(ABC):

    @abstractmethod
    def mutate(self,sample:str)->str:
        raise NotImplementedError

    @abstractmethod
    def get_name(self):
        raise NotImplementedError

    def mutate_batch(self,sample_list:List):
        for sample in sample_list:
          self.mutate_sample(sample)
