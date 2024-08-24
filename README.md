# Jailbreak-security

This GitHub project provides a comprehensive dataset and analysis of jailbreak attacks on large language models (LLMs), comparing the effectiveness of various jailbreak techniques against existing defense mechanisms. The project includes data on refined query-based methods, sophisticated prompt engineering, and cross-modal attacks, illustrating the vulnerabilities in LLMs' processing of prompts as inputs. Additionally, it evaluates the robustness of current defense strategies, highlighting gaps in security and offering insights into the development of more resilient models. The project serves as a valuable resource for researchers and developers aiming to enhance LLM security and mitigate the risks of unauthorized model manipulation.


### Attacks 

| Jailbreaks               | Technique                               | References                                                                                 | Status |
| ------------------------ | --------------------------------------- | -------------------------------------------------------------------------------------------| ------ |
| **Query Based Jailbreaking** | PAIR                                  | [Chao et al., 2023](https://example.com/pair)                                            | ❌     |
|                          | Competing Objectives                    | [Wei et al., 2023](https://example.com/competing-objectives)                               | ❌     |
| **Prompt Engineering**   | DeepInception                           | [Li et al., 2023c](https://example.com/deepinception)                                      | ❌     |
|                          | ReNeLLM                                 | [Ding et al., 2023](https://example.com/renellm)                                           | ❌     |
| **Cross-Modal Attacks**  | Visual Adversarial Examples             | [Qi et al., 2023a](https://example.com/visual-adversarial-examples)                        | ❌     |
|                          | Low Resource Jailbreaking               | [Yong et al., 2023](https://example.com/low-resource-jailbreaking)                         | ❌     |
| **Universal Attacks**    | Universal Jailbreaks on Aligned LLMs    | [Qi et al., 2023a](https://example.com/universal-jailbreaks-on-aligned-llms)               | ❌     |
|                          | Tree of Attacks                         | [Mehrotra et al., 2023](https://example.com/tree-of-attacks)                               | ❌     |
|                          | Persona Modulation                      | [Shah et al., 2023b](https://example.com/persona-modulation)                               | ❌     |

### Defences

| Mitigation Strategy       | Technique                                | References                                                             | Status |
| ------------------------- | ---------------------------------------- | ---------------------------------------------------------------------- | ------ |
| **Input/Output Censorship** | Baseline Defenses                        | [Jain et al., 2023](https://example.com/baseline-defenses)              | ❌     |
|                           | SmoothLLM                                | [Robey et al., 2023](https://example.com/smoothllm)                    | ❌     |
|                           | Adversarial Prompt Shield                | [Kim et al., 2023](https://example.com/adversarial-prompt-shield)       | ❌     |
|                           | Llama Guard                              | [Inan et al., 2023](https://example.com/llama-guard)                    | ❌     |
|                           | NeMo-Guardrails                          | [Rebedea et al., 2023](https://example.com/nemo-guardrails)             | ❌     |
|                           | Self-Examination                         | [Helbling et al., 2023](https://example.com/self-examination)           | ❌     |
| **Model Training/Fine-Tuning** | Llama-2                              | [Touvron et al., 2023](https://example.com/llama-2)                    | ❌     |
|                           | Context-Distillation                     | [Askell et al., 2021](https://example.com/context-distillation)         | ❌     |


### Metrics

| Metric                        | Definition                                                                | Importance                                                              | Type     |
|-------------------------------|---------------------------------------------------------------------------|-------------------------------------------------------------------------|----------|
| **Attack Success Rate (ASR)** | Percentage of adversarial inputs that successfully fool the model.        | Higher ASR indicates a more effective attack.                           | Attack   |
| **Perturbation Magnitude**    | Degree of change applied to the original input, measured by norms like L2 or L∞. | Lower magnitude indicates a subtler, harder-to-detect attack.          | Attack   |
| **Query Efficiency**          | Number of queries made to the model during the attack.                    | Fewer queries indicate a more efficient attack, important in black-box scenarios. | Attack   |
| **Transferability Rate**      | Success rate of adversarial examples on different models.                 | Higher transferability means the attack is more generalized.            | Attack   |
| **Robustness to Defenses**    | How well the attack bypasses existing defense mechanisms.                 | Effective attacks remain potent despite defenses.                      | Attack   |
| **Defense Success Rate (DSR)**| Percentage of adversarial inputs correctly classified after applying the defense. | Higher DSR indicates a more effective defense.                         | Defense  |
| **Model Accuracy**            | Overall accuracy on clean and adversarially perturbed inputs post-defense. | A good defense maintains high accuracy on clean inputs while improving robustness. | Defense  |
| **Computational Overhead**    | Additional computational resources required to implement the defense.     | Lower overhead makes the defense more practical for real-time use.      | Defense  |
| **Adversarial Robustness (AR)**| Decrease in model accuracy when subjected to adversarial examples.        | A robust defense should minimize AR, ensuring stable model performance. | Defense  |
| **Generalization Across Attacks** | Defense effectiveness against a variety of attack techniques.           | A good defense should protect against multiple adversarial strategies.  | Defense  |


---

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
