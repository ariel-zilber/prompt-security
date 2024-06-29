
from abc import ABC, abstractmethod
from ast import List


class PromptEvaluator(ABC):
    @abstractmethod
    def eval_sample(self,sample):
        pass
    @abstractmethod
    def get_name(self):
        pass


    def eval_batch(self,sample_list:List):
        for sample in sample_list:
          self.eval_sample(sample)
