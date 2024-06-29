from prompt_security.evaluators.base import PromptEvaluator
from sentence_transformers import SentenceTransformer
import numpy as np

class MiniLMEmbeddingPromptEvaluator(PromptEvaluator):
    def __init__(self) -> None:
       super().__init__()
       self.model=SentenceTransformer('sentence-transformers/all-MiniLM-L12-v2')
    def eval_sample(self,sample):
        try:
          return self.model.encode([sample])
        except Exception as err:
          return np.nan


    def get_name(self):
        return 'Embedding'

