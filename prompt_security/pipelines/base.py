from typing import List
import os
import tqdm
import pickle
from collections import defaultdict
import pandas as pd
from prompt_security.utils.common import get_sig


class Pipeline:
    def __init__(self, mutators, evaluators,cache_folder,output_folder):
        self.mutators=mutators
        self.evaluators=evaluators
        self.cache_folder=cache_folder
        self.output_folder=output_folder
        

    def load_results(self,output_path):
        result=defaultdict(list)
        if os.path.exists(output_path):
            with open(output_path,'rb') as f:
                result=pickle.load(f)
        return result

    def mutate(self,prompts,output_path):
        result=self.load_results(output_path)

        for i in tqdm.tqdm(range(len(prompts))):
            if i in result["idx"]:
                print(i)
                continue

            result['idx'].append(i)
            result['Prompt'].append(prompts[i])
        
            # 
            mutated_prompt=prompts[i]
            names_of_mutations=[]
            for mutator in self.mutators:
                mutated_prompt=mutator.mutate(mutated_prompt)
                names_of_mutations.append(mutator.get_name())
            result['MutatedPrompt'].append(mutated_prompt)
            result['NamesOfMutations'].append("|".join(names_of_mutations))

            # save changes
            with open(output_path,'wb') as f:
                pickle.dump(result, f, protocol=pickle.HIGHEST_PROTOCOL)

        return pd.DataFrame.from_dict(result)


    def evaluate(self,prompts,output_path):
        result=self.load_results(output_path)

        for i in tqdm.tqdm(range(len(prompts))):
            if i in result["idx"]:
                continue

            prompt=prompts[i]
            result['idx'].append(i)
            result['MutatedPrompt'].append(prompt)
            for evaluator in self.evaluators:
                result[evaluator.get_name()].append(evaluator.eval_sample(prompt))

            with open(output_path,'wb') as f:
                pickle.dump(result, f, protocol=pickle.HIGHEST_PROTOCOL)
                
        return pd.DataFrame.from_dict(result)

        
    def run(self, prompts, output_file_name):

        mutated_data=[]
        output_path_mutate=self.cache_folder+'/'+output_file_name+"_tmp_mutate.pkl"
        output_path_evaluate=self.cache_folder+'/'+output_file_name+"_tmp_evaluate.pkl"
        output_path_result=self.output_folder+'/'+output_file_name+".csv"
        mutated_data=self.mutate(prompts,output_path_mutate)
        mutated_prompts=mutated_data['MutatedPrompt'].tolist()
        mutated_prompts_names=mutated_data['NamesOfMutations'].tolist()
        
        results=self.evaluate(mutated_prompts,output_path_evaluate).drop(columns=['idx'])
        results['Prompt']=[p for p in prompts]
        results['sha256']=[get_sig(p) for p in prompts]
        results['NamesOfMutations']=mutated_prompts_names
        results.to_csv(output_path_result)
        return results
       
        
    