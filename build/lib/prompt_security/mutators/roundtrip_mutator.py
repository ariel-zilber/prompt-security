

from prompt_security.mutators.base import PromptMutator
from transformers import MarianMTModel, MarianTokenizer


class RoundTripPromptMutator(PromptMutator):
  def __init__(self,model_name_translate='Helsinki-NLP/opus-mt-en-zh',model_name_inv_translate='Helsinki-NLP/opus-mt-zh-en',label=None):
    self.model_name_translate=model_name_translate
    self.model_name_inv_translate=model_name_inv_translate
    
    # Load the pre-trained model and tokenizer
    self.model_translate = MarianMTModel.from_pretrained(model_name_translate)
    self.tokenizer_translate = MarianTokenizer.from_pretrained(model_name_translate)

    # Load the pre-trained model and tokenizer
    self.model_inv_translate = MarianMTModel.from_pretrained(model_name_inv_translate)
    self.tokenizer_inv_translate = MarianTokenizer.from_pretrained(model_name_inv_translate)
    if label is None:
       self.label= f'RoundTripPromptMutator-{self.model_name_translate}--{self.model_name_translate}'
    else:
       self.label= f'RoundTripPromptMutator-{label}'
       

  def to_lang(self,text):
    inputs = self.tokenizer_translate.encode(text, return_tensors='pt', padding=True, truncation=True)
    translated_tokens = self.model_translate.generate(inputs, max_length=40, num_beams=4, early_stopping=True)
    translated_text = self.tokenizer_translate.decode(translated_tokens[0], skip_special_tokens=True)
    return translated_text

  def from_lang(self,text):
    inputs = self.tokenizer_inv_translate.encode(text, return_tensors='pt', padding=True, truncation=True)
    translated_tokens = self.model_inv_translate.generate(inputs, max_length=40, num_beams=4, early_stopping=True)
    translated_text = self.tokenizer_inv_translate.decode(translated_tokens[0], skip_special_tokens=True)
    return translated_text
  def mutate(self,sample:str)->str:
      return self.from_lang(self.to_lang(sample))

  def get_name(self):
      return self.label

