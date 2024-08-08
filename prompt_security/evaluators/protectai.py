
import requests
import json
import hashlib
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
from prompt_security.evaluators.base import PromptEvaluator
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

class ProtectAIDebertaV3BasePromptInjectionV2JudgeEvaluator(PromptEvaluator):
  def __init__(self):
    self.tokenizer = AutoTokenizer.from_pretrained("protectai/deberta-v3-base-prompt-injection-v2")
    self.model = AutoModelForSequenceClassification.from_pretrained("protectai/deberta-v3-base-prompt-injection-v2")
    self.classifier = pipeline(
            "text-classification",
            model=self.model,
            tokenizer=self.tokenizer,
            truncation=True,
            max_length=512,
            device=torch.device("cuda" if torch.cuda.is_available() else "cpu"))


  def eval_sample(self,sample:str)->str:
      return  self.classifier(sample) 

  def get_name(self):
      return 'ProtectAIDebertaV3BasePromptInjectionV2JudgeEvaluator'
  
  

class ProtectAIDebertaV3BasePromptInjectionJudgeEvaluator(PromptEvaluator):
  def __init__(self):
    self.tokenizer = AutoTokenizer.from_pretrained("protectai/deberta-v3-base-prompt-injection")
    self.model = AutoModelForSequenceClassification.from_pretrained("protectai/deberta-v3-base-prompt-injection")
    self.classifier = pipeline(
            "text-classification",
            model=self.model,
            tokenizer=self.tokenizer,
            truncation=True,
            max_length=512,
            device=torch.device("cuda" if torch.cuda.is_available() else "cpu"))
  def eval_sample(self,sample:str)->str:
      return  self.classifier(sample) 

  def get_name(self):
      return 'ProtectAIDebertaV3BasePromptInjectionV2JudgeEvaluator'
    
  
