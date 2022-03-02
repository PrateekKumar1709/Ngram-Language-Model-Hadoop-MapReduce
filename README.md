# Ngram-Language-Model-Hadoop-Map-Reduce

## Overview:

In the simplest form, a language models describes the probability of words appearing in a sentence. A unigram models the probability of a single word appearing in the corpus, while a bigram models the
probability of two words appearing in an exact sequence. An n-gram, then, models the probability of a sequence of n words appearing consecutively.
See https://www.techtarget.com/searchenterpriseai/definition/language-modeling#:~:text=Language%20modeling%20(LM)%20is%20the,basis%20for%20their%20word%20predictions.

As an example, given the following text (as the entire universe of words): “The Cat in the Hat is the best cat in the hat”, a unigram language model would be: (using fractions for clarity)the, 4/6
cat, 2/6
in, 2/6
hat, 2/6
is, 1/6
best, 1/6

A bigram (n-gram, n=2) count would be:
the cat, 1/8
cat in, 2/8
in the, 2/8
the hat, 2/8
hat is, 1/8
is the, 1/8
the best, 1/8
best cat, 1/8

For unigrams, no words precede the n-gram, so the probability of ‘cat’ appearing anywhere in the corpus is 2/6 using maximum likelihood estimation (MLE, note this is a very simplistic model – the closed
universe model). For bigrams, we could say that the probability of the phrase ‘the cat’ is 1/8.

The project aims to compute the unigrams, bigrams and trigram probabilities in the input text provided.
