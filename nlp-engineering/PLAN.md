# NLP Engineering: From Scratch to Expert

**Goal:** Rebuild deep, hands-on NLP expertise — every concept implemented from scratch before using a library.

**Philosophy:**
- Build it before you import it. If you can't implement it, you don't understand it.
- Every notebook ends with: "What breaks? What are the limits of this approach?"
- Progress linearly. Each module builds on the last.

---

## How to Study

1. **Read the concept** — understand what problem it solves and why it was invented
2. **Implement from scratch** in numpy/pure Python — no sklearn, no HuggingFace, no shortcuts
3. **Test on real text** — use actual datasets, not toy examples
4. **Break it** — find edge cases, failure modes, limitations
5. **Then use the library version** — appreciate what it adds, benchmark against your impl
6. **Write a 3-line summary** at the end of each notebook: what it does, when to use it, what breaks it

---

## Curriculum

### Module 01 — Text Fundamentals
*The plumbing. Every NLP system runs on this.*

| # | Topic | Build From Scratch | Key Question |
|---|-------|-------------------|--------------|
| 1.1 | Unicode, encoding, character sets | A string normalizer | Why does `"café" != "café"` sometimes? |
| 1.2 | Regex for NLP | Email/URL/mention extractor | What can't regex parse? |
| 1.3 | Tokenization — whitespace, rule-based | Your own tokenizer | Where does word boundary detection fail? |
| 1.4 | Byte Pair Encoding (BPE) | BPE tokenizer trained on a corpus | Why did GPT switch from words to BPE? |
| 1.5 | Normalization: stemming vs lemmatization | Porter stemmer | When does stemming hurt retrieval? |
| 1.6 | Sentence segmentation | Rule-based sentence splitter | What breaks naive period-splitting? |

**Datasets to use:** Project Gutenberg books, Wikipedia dump (small), your own notes

---

### Module 02 — Classical Retrieval
*The backbone of search. Still used in production everywhere.*

| # | Topic | Build From Scratch | Key Question |
|---|-------|-------------------|--------------|
| 2.1 | Inverted index | Build an inverted index from documents | How does posting list intersection work? |
| 2.2 | TF-IDF | TF-IDF vectorizer + cosine similarity search | Why does IDF suppress common words? |
| 2.3 | BM25 | Full BM25 scorer (k1, b params) | What do k1 and b actually control? |
| 2.4 | Query expansion | Synonym expansion with a thesaurus | When does expansion hurt precision? |
| 2.5 | Evaluation: precision, recall, NDCG | Implement all metrics from scratch | What does NDCG tell you that MAP doesn't? |

**Project:** Build a search engine over a Wikipedia subset. Compare TF-IDF vs BM25. Measure NDCG.

---

### Module 03 — Classical ML for Text
*Before neural nets. Still competitive on small data.*

| # | Topic | Build From Scratch | Key Question |
|---|-------|-------------------|--------------|
| 3.1 | Naive Bayes for text classification | Multinomial NB | Why does Laplace smoothing matter? |
| 3.2 | Logistic Regression with bag-of-words | LR + gradient descent on text features | Why does LR beat NB on many tasks? |
| 3.3 | N-gram language models | Bigram/trigram LM with add-k smoothing | What is perplexity measuring? |
| 3.4 | Edit distance & fuzzy matching | Levenshtein + dynamic programming | How does spell correction work? |
| 3.5 | CRF for sequence labeling | Viterbi decoding for POS/NER | Why do CRFs outperform HMMs for NER? |

**Project:** Spam classifier (NB vs LR). Spell corrector. POS tagger.

---

### Module 04 — Word Vectors
*The first real shift. Meaning as geometry.*

| # | Topic | Build From Scratch | Key Question |
|---|-------|-------------------|--------------|
| 4.1 | Co-occurrence matrices + PMI | PMI matrix from corpus | What's the geometric intuition of PMI? |
| 4.2 | Word2Vec — Skip-gram | Skip-gram with negative sampling in numpy | Why is negative sampling an approximation? |
| 4.3 | Word2Vec — CBOW | CBOW training loop | When does CBOW beat skip-gram? |
| 4.4 | GloVe | GloVe objective + weighted least squares | What does GloVe optimize that W2V doesn't? |
| 4.5 | FastText | Subword embeddings | How does FastText handle OOV? |
| 4.6 | Analogy tasks & intrinsic eval | Implement word analogy eval | Why do intrinsic evals not predict downstream? |

**Project:** Train Word2Vec on a domain corpus. Evaluate analogies. Visualize with t-SNE.

---

### Module 05 — Sequence Models
*Modeling order. The step before attention.*

| # | Topic | Build From Scratch | Key Question |
|---|-------|-------------------|--------------|
| 5.1 | RNN forward + backprop through time | Vanilla RNN in numpy | Why does BPTT cause vanishing gradients? |
| 5.2 | LSTM | LSTM cell from scratch (gates in numpy) | Which gate prevents vanishing gradients? |
| 5.3 | GRU | GRU cell | Why is GRU faster than LSTM? |
| 5.4 | Seq2Seq with encoder-decoder | Seq2Seq in PyTorch | What's the information bottleneck problem? |
| 5.5 | Beam search | Beam search decoder | How does beam width trade quality vs speed? |

**Project:** Character-level language model. Seq2Seq transliteration.

---

### Module 06 — Attention & Transformers
*The architecture that won. Understand every line.*

| # | Topic | Build From Scratch | Key Question |
|---|-------|-------------------|--------------|
| 6.1 | Bahdanau attention | Attention over encoder hidden states | What does the attention weight matrix look like? |
| 6.2 | Scaled dot-product attention | Q/K/V in numpy | Why scale by √d_k? |
| 6.3 | Multi-head attention | MHA in PyTorch from scratch | What does each head learn? |
| 6.4 | Positional encoding | Sinusoidal PE + learned PE | Why doesn't the transformer "see" order by default? |
| 6.5 | Full Transformer encoder | Build from the paper (Vaswani 2017) | What does LayerNorm actually stabilize? |
| 6.6 | Full Transformer decoder + causal mask | Autoregressive generation | Why does the causal mask matter at inference? |
| 6.7 | Mini-GPT | Small GPT trained on Shakespeare | What does next-token prediction actually learn? |

**Project:** Implement the full Transformer. Train a character-level GPT. Generate text.

---

### Module 07 — Modern NLP
*Using the big models. Fine-tuning, prompting, retrieval.*

| # | Topic | What to Build | Key Question |
|---|-------|---------------|--------------|
| 7.1 | BERT architecture deep dive | Annotate every line of BERT forward pass | What is [CLS] actually learning? |
| 7.2 | Fine-tuning BERT | Fine-tune on classification + NER | When does full fine-tune beat LoRA? |
| 7.3 | Sentence embeddings + semantic search | Bi-encoder with FAISS index | What's the difference between bi- and cross-encoder? |
| 7.4 | Dense retrieval (DPR) | Train a bi-encoder retriever | Why does BM25 still beat dense on many datasets? |
| 7.5 | RAG — Retrieval Augmented Generation | Build RAG from scratch (no LangChain) | What are the failure modes of naive RAG? |
| 7.6 | LoRA fine-tuning | Fine-tune a small LLM with LoRA | What is the rank r controlling? |
| 7.7 | Prompting & few-shot | Chain-of-thought, few-shot classification | When does prompting beat fine-tuning? |

**Project:** Build a domain-specific QA system with RAG. Evaluate retrieval and generation separately.

---

### Module 08 — Evaluation & Production
*How to measure it. How to ship it.*

| # | Topic | Build / Instrument | Key Question |
|---|-------|-------------------|--------------|
| 8.1 | Text classification metrics | F1, macro/micro, confusion matrix | When is macro-F1 misleading? |
| 8.2 | Generation metrics: BLEU, ROUGE, BERTScore | Implement BLEU from scratch | Why is BLEU a poor metric for open generation? |
| 8.3 | LLM evaluation: LLM-as-judge | Build an eval harness with Claude API | What biases does LLM-as-judge introduce? |
| 8.4 | Latency & cost profiling | Profile your RAG pipeline end-to-end | Where are the bottlenecks in a RAG system? |
| 8.5 | Serving: tokenization, batching, quantization | Run a model with llama.cpp or vLLM | What does INT8 quantization lose? |

---

## Recommended Order

```
Week 1-2:   Module 01 (Text Fundamentals) + Module 02 (Classical Retrieval)
Week 3:     Module 03 (Classical ML)
Week 4-5:   Module 04 (Word Vectors)
Week 6-7:   Module 05 (Sequence Models)
Week 8-10:  Module 06 (Attention & Transformers)  ← spend the most time here
Week 11-12: Module 07 (Modern NLP)
Week 13-14: Module 08 (Evaluation & Production)
```

---

## Resources Per Module

### Papers to read (in order)
- BM25: *Okapi BM25 (Robertson et al., 1994)*
- Word2Vec: *Efficient Estimation of Word Representations (Mikolov et al., 2013)*
- GloVe: *GloVe: Global Vectors for Word Representation (Pennington et al., 2014)*
- Attention: *Neural Machine Translation by Jointly Learning to Align and Translate (Bahdanau et al., 2015)*
- Transformer: *Attention Is All You Need (Vaswani et al., 2017)*
- BERT: *BERT: Pre-training of Deep Bidirectional Transformers (Devlin et al., 2018)*
- GPT: *Language Models are Few-Shot Learners (Brown et al., 2020)*
- LoRA: *LoRA: Low-Rank Adaptation of Large Language Models (Hu et al., 2021)*
- RAG: *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks (Lewis et al., 2020)*

### Books
- *Speech and Language Processing* — Jurafsky & Martin (free online, 3rd ed draft)
- *Natural Language Processing with PyTorch* — Rao & McMahan

---

## Rules for Each Notebook

1. Start with: "What problem does this solve? Why was it invented?"
2. Implement the core algorithm before any library call
3. Test on at least 2 different datasets or inputs
4. End with: "Limitations / when not to use this"
5. Benchmark your impl against the library version (speed + correctness)

---

## Progress Tracker

- [ ] 01.1 Unicode & encoding
- [ ] 01.2 Regex for NLP
- [ ] 01.3 Rule-based tokenization
- [ ] 01.4 BPE tokenizer
- [ ] 01.5 Stemming & lemmatization
- [ ] 01.6 Sentence segmentation
- [ ] 02.1 Inverted index
- [ ] 02.2 TF-IDF search
- [ ] 02.3 BM25
- [ ] 02.4 Query expansion
- [ ] 02.5 Retrieval evaluation metrics
- [ ] 03.1 Naive Bayes
- [ ] 03.2 Logistic Regression for text
- [ ] 03.3 N-gram language models
- [ ] 03.4 Edit distance & spell correction
- [ ] 03.5 CRF for sequence labeling
- [ ] 04.1 PMI co-occurrence
- [ ] 04.2 Word2Vec skip-gram
- [ ] 04.3 Word2Vec CBOW
- [ ] 04.4 GloVe
- [ ] 04.5 FastText
- [ ] 04.6 Analogy evaluation
- [ ] 05.1 Vanilla RNN
- [ ] 05.2 LSTM
- [ ] 05.3 GRU
- [ ] 05.4 Seq2Seq
- [ ] 05.5 Beam search
- [ ] 06.1 Bahdanau attention
- [ ] 06.2 Scaled dot-product attention
- [ ] 06.3 Multi-head attention
- [ ] 06.4 Positional encoding
- [ ] 06.5 Transformer encoder
- [ ] 06.6 Transformer decoder
- [ ] 06.7 Mini-GPT
- [ ] 07.1 BERT deep dive
- [ ] 07.2 BERT fine-tuning
- [ ] 07.3 Sentence embeddings + FAISS
- [ ] 07.4 Dense retrieval (DPR)
- [ ] 07.5 RAG from scratch
- [ ] 07.6 LoRA fine-tuning
- [ ] 07.7 Prompting & few-shot
- [ ] 08.1 Classification metrics
- [ ] 08.2 Generation metrics
- [ ] 08.3 LLM-as-judge eval harness
- [ ] 08.4 Latency profiling
- [ ] 08.5 Model serving
