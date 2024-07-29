
import requests
import json
import hashlib
from transformers import AutoTokenizer, AutoModelForSequenceClassification,AutoModelForPreTraining
import torch
from prompt_security.evaluators.base import PromptEvaluator

from transformers import MobileBertTokenizer, MobileBertForSequenceClassification


class SQLInjectionRoBERTJudgeEvaluator(PromptEvaluator):
  def __init__(self):
    self.tokenizer = MobileBertTokenizer.from_pretrained('google/mobilebert-uncased')
    self.model = MobileBertForSequenceClassification.from_pretrained('cssupport/mobilebert-sql-injection-detect')

    self.model.to('cpu')
    self.model.eval()


  def predict(self, text: str)->tuple:
    inputs = self.tokenizer(text, padding=False, truncation=True, return_tensors='pt', max_length=512)
    input_ids = inputs['input_ids'].to('cpu')
    attention_mask = inputs['attention_mask'].to('cpu')

    with torch.no_grad():
        outputs = self.model(input_ids=input_ids, attention_mask=attention_mask)

    logits = outputs.logits
    probabilities = torch.softmax(logits, dim=1)
    predicted_class = torch.argmax(probabilities, dim=1).item()
    return predicted_class, probabilities[0][predicted_class].item()


  def eval_sample(self,sample:str)->str:
    predicted_class, confidence = self.predict(sample)
    return predicted_class 

  def get_name(self):
      return 'RobertaJudge'