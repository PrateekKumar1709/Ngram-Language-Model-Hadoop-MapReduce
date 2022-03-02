#!/usr/bin/env python
import sys
import re

def test_mapper():
    
    lines = (sys.stdin)
    sep = '\t'
    
    for line in lines:
        line = re.sub(r'[^0-9a-z]', ' ', line.lower())
        line_len = len (line)
        if line_len < 3:
            continue
        words = re.split(r' +', line)
        words.remove('')
        length = len(words)
        
        i = 0
        while (i < length):
            first = words[i]
            unigram = "%s %s %s %d \n" % (first, 'bd-22-unigram', sep, 1)
            sys.stdout.write(unigram)
            i += 1
        
        j = 0
        while (j+1 < length):
            first = words[j]
            second = words [j+1]
            bigram = "%s %s %s %s %d \n" % (first, second, 'bd-22-bigram', sep, 1)
            sys.stdout.write(bigram)
            j += 1
        
        k = 0
        while (k+2 < length):
            first = words[k]
            second = words [k+1]
            third = words[k+2]
            trigram = "%s %s %s %s %s %d  \n" % (first, second, third, 'bd-22-trigram', sep, 1)
            sys.stdout.write(trigram)
            k += 1
            
if __name__ == "__main__":
    test_mapper()
