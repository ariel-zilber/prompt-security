
import hashlib
from prompt_security.evaluators.gpt2_perplexity import GPT2PerplexityEvaluator
from prompt_security.evaluators.gpt2_sequence_length import GPT2SequenceLengthPromptEvaluator
from prompt_security.evaluators.mini_llm_perplexity import MiniLMEmbeddingPromptEvaluator
from prompt_security.evaluators.sha256_evaluator import Sha256PromptEvaluator
from prompt_security.evaluators.utils import evaluate_all
from prompt_security.mutators.llm_mutator import AttackerLLMBasicPromptMutator
from prompt_security.mutators.roundtrip_mutator import RoundTripPromptMutator
from prompt_security.mutators.typo_mutator import TypoPromptMutator
from prompt_security.mutators.utils import mutate_all
import pandas as pd


def get_sig(sample:str)->str:
    # Encode the text to bytes
    text_bytes = sample.encode('utf-8')

    # Create a sha256 hash object
    sha256_hash = hashlib.sha256()

    # Update the hash object with the bytes
    sha256_hash.update(text_bytes)

    # Get the hexadecimal representation of the hash
    hash_hex = sha256_hash.hexdigest()

    return hash_hex

mutators=[
    TypoPromptMutator(0.05),
    TypoPromptMutator(0.1),
    TypoPromptMutator(0.2),
    AttackerLLMBasicPromptMutator(),
    RoundTripPromptMutator(label="en->ch->en")
]
evaluators=[
    GPT2PerplexityEvaluator(),
    GPT2SequenceLengthPromptEvaluator(),
    MiniLMEmbeddingPromptEvaluator()
]


texts=["Hello my friend"]

def generate_dataset(texts,file_name):
    data=[]
    original=[]
    idx_list=[]
    sigs=[]
    for _,row in mutate_all(texts,mutators,file_name+"tmp_mutate.pkl").iterrows():
        idx=row['idx']
        original_prompt=row['Prompt']
        
        prompts_variations=(row.values[2:])
        for prompt_variation in prompts_variations:
            idx_list.append(idx)
            data.append(prompt_variation)
            original.append(original_prompt)
            sigs.append(get_sig(original_prompt))

    results=evaluate_all(data,evaluators,file_name+"tmp_evaluate.pkl")
    results['idx']=idx
    results['Original_Prompt']=original
    results['sha256']=sigs
    results.to_csv(file_name+".csv")
    return results


generate_dataset(texts,"example")