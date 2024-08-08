
from prompt_security.evaluators.base import PromptEvaluator
from sentence_transformers import SentenceTransformer



DEFAULT_MODEL_NAME = 'sentence-transformers/all-MiniLM-L12-v2'


class SentanceEmbeddingEvaluator(PromptEvaluator):
  def __init__(self,device='cpu',model_name=DEFAULT_MODEL_NAME) -> None:
    self.device = device
    self.model  =  SentenceTransformer(model_name,device=device)
    
  def eval_sample(self,sample:str)->str:
      return  self.model.encode([sample])

  def get_name(self):
      return 'Embedding'