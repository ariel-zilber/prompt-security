import os
import pickle
from tqdm import tqdm
from typing import List
import pandas as pd
from prompt_security.evaluators.base import PromptEvaluator

def init_evaluator_result_object(output_path,evaluator_list):
  result={'idx':[],'Prompt':[]}
  if os.path.exists(output_path):
    with open(output_path,'rb') as f:
      result=pickle.load(f)

  if os.path.exists(output_path):
    with open(output_path,'rb') as f:
      result=pickle.load(f)

  for evaluator in evaluator_list:
    result[evaluator.get_name()]=result.get(evaluator.get_name(),[])


  return result

def evaluate_all(prompts,evaluator_list:List[PromptEvaluator],output_path):
  result=init_evaluator_result_object(output_path,evaluator_list)

  for i in tqdm(range(len(prompts))):
    if i in result["idx"]:
      continue

    prompt=prompts[i]
    result['idx'].append(i)
    result['Prompt'].append(prompt)
    for evaluator in evaluator_list:
      result[evaluator.get_name()].append(evaluator.eval_sample(prompt))

    with open(output_path,'wb') as f:
      pickle.dump(result, f, protocol=pickle.HIGHEST_PROTOCOL)
  return pd.DataFrame.from_dict(result)

