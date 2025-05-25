# Advanced Methods in Text Analytics

This repository contains teaching materials for the course 
[Advanced Methods in Text Analytics](https://www.uni-mannheim.de/dws/teaching/course-details/courses-for-master-candidates/ie-696-advanced-methods-in-text-analytics/), a MSc 
course created by 
[Daniel Ruffinelli](https://www.uni-mannheim.de/dws/people/researchers/postdoctoral-research-fellows/daniel-ruffinelli/) for the 
[University of Mannheim](https://www.wim.uni-mannheim.de/en/). 
The course is designed to cover the latest methods for natural language 
processing (NLP), and so is heavily focused on language models in general, and 
large language models (LLMs) in particular. 
These teaching materials are released under a 
[Creative Commons CC-By license](https://creativecommons.org/licenses/by/4.0/)
for free use for educational purposes and include [lecture slides](lectures/) in 
PDF and PPTX, as well as [exercises](tutorials/) in PDF and TEX.

## Course Design

* The course is designed for the average MSc student I've taught for years as
    a Teaching Assistant in Machine Learning and Deep Learning courses.
* The course assumes (and thus only quickly refreshes) BSc-level concepts from 
    probability theory, linear algebra and calculus, as well as having taken a 
    Machine Learning course that covers things like model training and 
    evaluation.
    Deep Learning knowledge is also recommended, but is technically not 
    necessary, as such concepts are discussed in more depth as needed.
    So depending on your background, you may find this material more or less 
    challenging.
* This material is designed to be used for self-study (what I liked as a 
    student). Consequently, lecture slides are readable but text-heavy (and PPTX
    files are animated so each bullet point appears separately), and exercise 
    solutions are rather verbose.
* Generally, lectures are designed to refresh known concepts, introduce new 
    concepts, present important methods in detail, and briefly cover the latest 
    research on some of these topics. 
    The lectures are full of references throughout, as well as in the final
    References slide.
* The purpose of exercise sheets is more versatile, as these are sometimes used
    to dive deeper into some concepts introduced in the lectures, but are also 
    often used to introduce new but very important concepts that are perhaps 
    better discussed in a hands-on approach. 
    In other words, exercise sheets are as important as lecture slides. Also, a 
    few exercise sheets are focused on coding tasks designed to help internalize 
    many of the concepts discussed throughout the course.
* All images should have a link to their source, except those coming from the
    main reference book 
    ([Jurafsky et al. (2025)](https://web.stanford.edu/~jurafsky/slp3/)) or 
    where it clear from context (e.g. the source paper is introduced in the same
    slide).

## Lectures

1. [Introduction](lectures/01_introduction/)
    * Classic vs modern NLP
    * Basic NLP Concepts
2. [ML, DL and Word Embeddings](lectures/02_ml_dl_word_embeddings/)
    * Machine Learning Refresher
    * Deep Learning Basics
    * Word Embeddings
3. [RNNs](lectures/03_rnns/)
    * Recursive Neural Networks
    * Language Modeling with Recursive Neural Networks (teacher forcing, vanishing gradients)
    * LSTMs
    * Encoder-Decoder Architecture
    * Attention
4. [Transformers](lectures/04_transformers/)
    * Attention Revisited
    * Self-Attention
    * The Transformer Architecture
5. [Transfer Learning](lectures/05_transfer_learning/)
    * Language Modeling with Transformers
    * Masked Language Models (BERT)
    * Causal Language Models (the GPT family)
    * Fine-tuning (PEFT, adapters)
6. [Tokenization](lectures/06_tokenization/)
    * Role and Impact of Tokenization
    * Few tokenization methods (BPE, UnigramLM, SentencePiece)
7. [Large Language Models](lectures/07_llms/)
    * In-Context Learning (prompting, CoT)
    * LLM Architectures (the GPT family, the Llama family)
    * Model distillation, mixture-of-experts, scaling laws
    * Instruction Tuning
    * Reinforcement Learning from Human Feedback (RLHF)
8. [NLP Applications](lectures/08_nlp_applications/)
    * LLM Evaluation (per-token likelihood, verbalizers, model-based metrics)
    * Evaluation Benchmarks (MMLU, Human Eval, etc.)
    * Real-world Applications (work in progress)
9. [Multilingual NLP](lectures/09_multilingual_nlp/)
    * Cross-lingual transfer (embedding alignment, cross-lingual word embeddings)
    * Multilingual Transformers (training and tokenization in multilingual settings)
10. [State Space Models](lectures/10_state_space_models/)
    * State space models (discretization, structured state space models)
    * The Mamba Architecture
11. [Reasoning LLMs](lectures/11_reasoning_llms/)
    * Test-time compute
    * Vanilla vs Reasoning LLMs
    * Deepseek-R1

## Tutorials

* TODO list of tutorials with links

## Why Do I Make Exercise Solutions Public?

* To follow the open access practices that characterize Machine Learning 
    research.
* So that the materials are useful for self-study for any interested individual.
* I've used the exercise sheets as ungraded exercises, and I have found students 
    to happily work through the tasks by themselves before discussing the 
    solutions. 
* But yes, public solutions means the exercise sheets should not be used as 
    graded exercises. 

## TODO

* The course can still be significantly improved, e.g. many concepts introduced 
    throughout the course can be better illustrated.
* But I currently feel that adding the following is priority:
    * KV-Caching, Multi-Query Attention, Grouped-Query Attention, Multi-Latent 
        Attention
    * More recent approaches to positional embeddings, e.g. RoPE
    * Proper coverage of NLP Applications from 
    [Jurafsky et al. (2025)](https://web.stanford.edu/~jurafsky/slp3/) (the last
    section of the NLP Applications lecture is severely unfinished)

## How to Contribute

* Please create an issue to report any bugs you find in this material, from 
    typos and broken links to errors and important concepts that you think are
    missing.
