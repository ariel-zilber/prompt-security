
import random
import math
import string
from prompt_security.mutators.base import PromptMutator
import random
import nltk
from nltk.corpus import words

# Download the words corpus if you haven't already
nltk.download('words')
import random
import nltk
from nltk.corpus import words

# Download the word list if not already downloaded
nltk.download('words')



class RandomWordsPromptMutator(PromptMutator):
    def __init__(self,min_num_words=None,max_num_words=None,percentage=0.05):
        self.percentage=percentage
        self.min_num_words=min_num_words
        self.max_num_words=max_num_words

    def __insert_random_words(self,sentence):
        word_list = words.words()
        words_in_sentence = sentence.split()
        num_words = len(words_in_sentence)
        
        num_to_insert = int(num_words * self.percentage )
        
        if self.min_num_words is not None:
            num_to_insert = max(num_to_insert, self.min_num_words)
        
        if self.max_num_words is not None:
            num_to_insert=min(num_to_insert,self.max_num_words)
        
        random_words = random.sample(word_list, num_to_insert)
        
        for word in random_words:
            insert_position = random.randint(0, len(words_in_sentence))
            words_in_sentence.insert(insert_position, word)
        
        return ' '.join(words_in_sentence)

    def mutate(self,sample:str)->str:
        return self.__insert_random_words(sample)

    def get_name(self):
        return f'RandomWordsPromptMutator-{self.percentage}-{self.min_num_words}-{self.max_num_words}'




class PrefixRandomWordsPromptMutator(PromptMutator):
    def __init__(self,num_to_insert=3):
        self.num_to_insert=num_to_insert

    def __insert_random_words(self,sentence):
        word_list = words.words()
        words_in_sentence = sentence.split()
        random_words = random.sample(word_list, self.num_to_insert)
        words_in_sentence=random_words+words_in_sentence
        return ' '.join(words_in_sentence)

    def mutate(self,sample:str)->str:
        return self.__insert_random_words(sample)

    def get_name(self):
        return f'PrefixRandomWordsPromptMutator-{self.num_to_insert}'

class SuffixRandomWordsPromptMutator(PromptMutator):
    def __init__(self,num_to_insert=3):
        self.num_to_insert=num_to_insert

    def __insert_random_words(self,sentence):
        word_list = words.words()
        words_in_sentence = sentence.split()
        random_words = random.sample(word_list, self.num_to_insert)
        words_in_sentence=words_in_sentence+random_words
        return ' '.join(words_in_sentence)

    def mutate(self,sample:str)->str:
        return self.__insert_random_words(sample)

    def get_name(self):
        return f'SuffixRandomWordsPromptMutator-{self.num_to_insert}'
      

class ArbitraryLocationChunkRandomWordsPromptMutator(PromptMutator):
    def __init__(self,min_num_words=None,max_num_words=None,percentage=0.05):
        self.percentage=percentage
        self.min_num_words=min_num_words
        self.max_num_words=max_num_words

    def __insert_random_words(self,sentence):
        word_list = words.words()
        words_in_sentence = sentence.split()
        num_words = len(words_in_sentence)

        num_to_insert = int(num_words * self.percentage )

        if self.min_num_words is not None:
            num_to_insert = max(num_to_insert, self.min_num_words)

        if self.max_num_words is not None:
            num_to_insert=min(num_to_insert,self.max_num_words)

        random_words = random.sample(word_list, num_to_insert)
        insert_position = random.randint(0, len(words_in_sentence))
        for word in random_words:
            words_in_sentence.insert(insert_position, word)

        return ' '.join(words_in_sentence)

    def mutate(self,sample:str)->str:
        return self.__insert_random_words(sample)

    def get_name(self):
        return f'ArbitraryLocationChunkRandomWordsPromptMutator-{self.percentage}-{self.min_num_words}-{self.max_num_words}'

