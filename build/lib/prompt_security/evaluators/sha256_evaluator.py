

import hashlib
from prompt_security.evaluators.base import PromptEvaluator


class Sha256PromptEvaluator(PromptEvaluator):
  def __init__(self):
      pass

  def eval_sample(self,sample:str)->str:
    # Encode the text to bytes
    text_bytes = sample.encode('utf-8')

    # Create a sha256 hash object
    sha256_hash = hashlib.sha256()

    # Update the hash object with the bytes
    sha256_hash.update(text_bytes)

    # Get the hexadecimal representation of the hash
    hash_hex = sha256_hash.hexdigest()

    return hash_hex

  def get_name(self):
      return 'sha256'