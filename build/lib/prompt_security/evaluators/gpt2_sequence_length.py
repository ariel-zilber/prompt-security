
from gettext import npgettext
from prompt_security.evaluators.base import PromptEvaluator

from transformers import GPT2Tokenizer, GPT2LMHeadModel,GPT2Model



class GPT2SequenceLengthPromptEvaluator(PromptEvaluator):
    def __init__(self) -> None:
       super().__init__()

    def __calculate_sequence_length(self,sentence, model_name='gpt2'):
        # Load pre-trained model and tokenizer
        tokenizer = GPT2Tokenizer.from_pretrained(model_name)
        inputs = tokenizer(sentence, return_tensors='pt')
        return inputs['input_ids'].shape[1]

    def eval_sample(self,sample):
        try:
          return self.__calculate_sequence_length(sample)
        except Exception as err:
          print(err)

          return npgettext.nan

    def get_name(self):
        return 'Length'
