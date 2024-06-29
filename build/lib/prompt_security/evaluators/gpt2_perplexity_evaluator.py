from prompt_security.evaluators.base import PromptEvaluator
from transformers import GPT2Tokenizer, GPT2LMHeadModel,GPT2Model
import torch
import numpy as np

class GPT2PerplexityEvaluator(PromptEvaluator):
  def __init__(self,model_name='gpt2') -> None:
      super().__init__()
      self.model_name=model_name
      self.tokenizer_gpt2 = GPT2Tokenizer.from_pretrained('gpt2')
      self.model_gpt2 = GPT2LMHeadModel.from_pretrained('gpt2')

  def calculate_perplexity(self,sentence):
    inputs = self.tokenizer_gpt2(sentence, return_tensors='pt')
    input_ids = inputs['input_ids']
    with torch.no_grad():
        outputs = self.model_gpt2(input_ids, labels=input_ids)
    # Calculate the loss
    loss = outputs.loss
    perplexity = torch.exp(loss)
    return  perplexity


  def eval_sample(self,sample):
      try:
        return self.calculate_perplexity(sample)
      except Exception as err:
        print(err)
        return np.nan

  def get_name(self):
      return 'Perplexity'
