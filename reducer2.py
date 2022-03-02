#!/usr/bin/env python
from ngram_counter import * 
import os
import sys

#for line in sys.stdin:
for line in sys.stdin:
    line = line.strip()
        
    #ngram_length = ngram.count(' ') + 1

    if "bd-22-unigram" in line:
        line=line.replace('bd-22-unigram', '')
        ngram, count = line.split('\t')
        print("%s\t%s/%s" % (ngram, count, Unigrams))
        
    if "bd-22-bigram" in line:
        line=line.replace('bd-22-bigram', '')
        ngram, count = line.split('\t')
        print("%s\t%s/%s" % (ngram, count, Bigrams))
            
    if "bd-22-trigram" in line:
        line=line.replace('bd-22-trigram', '')
        ngram, count = line.split('\t')
        print("%s\t%s/%s" % (ngram, count, Trigrams))
            