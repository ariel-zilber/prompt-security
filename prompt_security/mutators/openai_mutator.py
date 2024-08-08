import requests
import json
from prompt_security.mutators.base import PromptMutator
from langchain import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


#
DEFAULT_FREQUENCY_PENALATY=0
DEFAULT_PRESENCE_PENALATY=0
DEFAULT_TOP_P=0.9
DEFAULT_TEMPERATURE=0.7
DEFAULT_MAX_TOKENS=256
DEFAULT_TEMPLATE="You are a helpful assistant. Answer the following question: {query}" 
DEFAULT_MODEL='gpt4'
# 


from langchain import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Define default values
DEFAULT_TEMPLATE = "You are a helpful assistant. Answer the following question: {query}"
DEFAULT_TEMPERATURE = 0.7
DEFAULT_MAX_TOKENS = 150
DEFAULT_TOP_P = 0.9
DEFAULT_FREQUENCY_PENALTY = 0.0
DEFAULT_PRESENCE_PENALTY = 0.0
DEFAULT_MODEL = 'gpt-4'
DEFAULT_STOP = None  # Add this if you want to use stop sequences
DEFAULT_LOGIT_BIAS = None  # Add this if you want to use logit bias
DEFAULT_USER = None  # Add this if you want to pass a user ID

def get_as_not_none(value):
  if value is None:
    return ''
  return value


class OpenAIBaseMutator(PromptMutator):
    def __init__(self,
                 api_key,
                 input_variables=["query"],
                 template=DEFAULT_TEMPLATE,
                 temperature=DEFAULT_TEMPERATURE,
                 top_p=DEFAULT_TOP_P,
                 model_name=DEFAULT_MODEL):
      
        self.model_name = model_name
        self.llm = OpenAI(
            api_key=api_key,
            model=self.model_name,
            temperature=temperature,
            top_p=top_p,
        )
        self.prompt_template = PromptTemplate(input_variables=input_variables, template=template)
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt_template)
        
        name_args=[
          'OpenAI',
           str(model_name),
           str( temperature),
            str(top_p)
            ]
        self.name="|".join(name_args)
    def mutate(self, sample: str) -> str:
        return self.chain.run(sample)

    def get_name(self):
        return self.name