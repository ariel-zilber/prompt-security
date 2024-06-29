import os
import pickle
import pandas as pd

from typing import List

import tqdm

from prompt_security.mutators.base import PromptMutator


def init_mutator_result_object(output_path,evaluator_list):
  result={'idx':[],'Prompt':[]}
  for evaluator in evaluator_list:
    result[evaluator.get_name()]=[]


  if os.path.exists(output_path):
    with open(output_path,'rb') as f:
      result=pickle.load(f)

  if os.path.exists(output_path):
    with open(output_path,'rb') as f:
      result=pickle.load(f)
  return result


def mutate_all(prompts,mutators_list:List[PromptMutator],output_path):
  result=init_mutator_result_object(output_path,mutators_list)

  for i in tqdm.tqdm(range(len(prompts))):
    if i in result["idx"]:
      continue

    prompt=prompts[i]
    result['idx'].append(i)
    result['Prompt'].append(prompt)
    for mutator in mutators_list:
      result[mutator.get_name()].append(mutator.mutate(prompt))

    with open(output_path,'wb') as f:
      pickle.dump(result, f, protocol=pickle.HIGHEST_PROTOCOL)

  return pd.DataFrame.from_dict(result)

