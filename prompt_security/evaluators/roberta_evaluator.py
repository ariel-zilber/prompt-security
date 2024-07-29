
import requests
import json
import hashlib
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
from prompt_security.evaluators.base import PromptEvaluator


class RobertaJudgeEvaluator(PromptEvaluator):
  def __init__(self):
    self.tokenizer = AutoTokenizer.from_pretrained("hubert233/GPTFuzz")
    self.model = AutoModelForSequenceClassification.from_pretrained("hubert233/GPTFuzz")


  def eval_sample(self,sample:str)->str:

      inputs = self.tokenizer([sample], padding=True, truncation=True,
                              max_length=512, return_tensors="pt").to('cpu')
      with torch.no_grad():
          outputs = self.model(**inputs)

      predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
      _, predicted_classes = torch.max(predictions, dim=1)
      return  predicted_classes.cpu().tolist()

  def get_name(self):
      return 'RobertaJudge'