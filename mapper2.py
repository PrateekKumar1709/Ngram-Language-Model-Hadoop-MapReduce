#!/usr/bin/env python
"""An advanced Mapper, using Python iterators and generators."""

import sys
import re
import io

#from numpy import outer

#ngrams = ["bd-22-unigram", "bd-22-bigram", "bd-22-trigram"]
unigram = 0
def main():
    
    unigram = 0
    bigram = 0
    trigram = 0
    
    lines = (sys.stdin)
    for line in lines:
        line=line.rstrip()
        if "bd-22-unigram" in line:
            unigram = unigram  + 1
            sys.stdout.write("\n"+line)
        elif "bd-22-bigram" in line:
            bigram = bigram  + 1
            sys.stdout.write("\n"+line)
        else:
            trigram = trigram  + 1
            sys.stdout.write("\n"+line)
                
    f = open("/home/prateek/Prateek/Courses/BigData/Assignments/A1/MR1/ngram_counter.py", "w")
    f.write("Unigrams =  '%d'\r\nBigrams = '%d'\r\nTrigrams = '%d'" % (unigram,bigram,trigram))
    f.close()

if __name__ == "__main__":
    main()
