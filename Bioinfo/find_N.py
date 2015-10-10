#Find and determines the number of occurences for indexes which have bad quality reads in fastq files

from readfastq import *
from collections import Counter

def findN(seqs):
    locs = []
    for seq in seqs:
        loc = seq.find('N')
        while(loc != -1):
            locs.append(loc)
            loc = seq.find('N', loc + 1)
    return Counter(locs)
