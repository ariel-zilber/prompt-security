# prompt-security

Prompt injection is a technique used to manipulate language models or AI systems by providing specially crafted input that causes the system to produce unintended or harmful responses. This form of attack leverages the model's reliance on user input to steer its behavior, potentially leading to security vulnerabilities, misinformation, or other detrimental outcomes. Understanding and mitigating prompt injection is crucial for ensuring the safe and reliable deployment of AI technologies.


Today, companies such [cloudflare](https://blog.cloudflare.com/firewall-for-ai)  offer solutions to detect prompt injections attacks , and interest in protection keeps increasing


This project offers an evaluation of 2 types of detectors

1. Perplexity based detector for GCG based attacks

Also we evaluate the capabilites of 3 types of detectors for general case(akin to signature based in WAF) attacks:
1. Transformers based detector
2. Classical nlp based detector
3. Embedding based detector


Moreover, we evaluate the strengths and weaknesses of each type of detector ,specfilally in relation to the following attack types:
* [GCG](https://arxiv.org/pdf/2307.15043)
* Peraphrase attack 


# Datasets
This project uses 3 datasets of adverserial samples:

* Peraphrase attack generation dataset : we use as a base couple of prompt injections and we generate variations using different  detection methods.The dataset can be found at : https://www.kaggle.com/datasets/arielzilber/prompt-injection-peraphrase-attack

* Suffix dataset : we follow the   [GCG](https://arxiv.org/pdf/2307.15043) paper and generate a suffix attack dataset.The dataset can be found at : https://www.kaggle.com/datasets/arielzilber/prompt-injection-suffix-attack

* Known prompt injection datasets : we gathered all the exisiting adverserial samples datasets avaliable on kaggle and on huggingface.The dataset can be found at : https://www.kaggle.com/datasets/arielzilber/prompt-injection-in-the-wild


And the following benign dataset:

https://www.kaggle.com/datasets/arielzilber/prompt-injection-benign-evaluation-framework

# Notebooks

1. [Dataset preprocessing](/notebooks/1_dataset_preproccessing.ipynb)

2. [generate adverserial suffix dataset](/notebooks/2_generate_adverserial_suffix_dataset.ipynb)

3. [perphrase attack generation](/notebooks/3_paraphrase_attack_generation.ipynb)

4. [EDA](/notebooks/4_eda.ipynb)

5. [Perplexity classifer](/notebooks/5_perplexity_classifer.ipynb)


6. [Embedding classifer](/notebooks/6_embedding_classifer.ipynb)


7. [Classical NLP classifer](/notebooks/7_nlp_classical_classifier.ipynb)


8. [Transformer classifer](/notebooks/8_nlp_modern_classifier.ipynb)
