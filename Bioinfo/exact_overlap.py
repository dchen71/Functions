#Finds the longest exact overlap (suffix/prefix match) between two strings

from overlap import *
from collections import defaultdict

def overlap_all_pairs(reads, min_length):
    kmer_dict = {}
    overlapping = []
    unique_read = set() #Use to find the number of unique nodes
    #Creates the kmers in the reads
    for read in reads:
        for i in range(len(read) - min_length + 1):
            kmer = read[i:i+ min_length]
            kmer_dict.setdefault(kmer, set()).add(read)

    #Scans the kmer suffixes and then calls overlap to find potential matches
    for read in reads:
        kmer = read[len(read) - min_length: len(read)]
        for scan in kmer_dict[kmer]:
            if overlap(read, scan, min_length) >= min_length and read != scan:
                overlapping.append((read,scan))
                unique_read.add(read)

    #run overlap and with dict key with its values, if equal 3 then it overlap and is good passing, need to figure out which to value to save though
    return overlapping

#Tests(Uses sets so answers will fluctuate without properly sorting it )
##Example 1
reads = ['ABCDEFG', 'EFGHIJ', 'HIJABC']
assert(overlap_all_pairs(reads, 3)) == [('ABCDEFG', 'EFGHIJ'), ('EFGHIJ', 'HIJABC'), ('HIJABC', 'ABCDEFG')]
assert(overlap_all_pairs(reads, 4)) == []
##Example 2
reads = ['CGTACG', 'TACGTA', 'GTACGT', 'ACGTAC', 'GTACGA', 'TACGAT']
assert(overlap_all_pairs(reads,5)) == [('CGTACG', 'GTACGT'), ('CGTACG', 'GTACGA'), ('TACGTA', 'ACGTAC'), ('GTACGT', 'TACGTA'), ('ACGTAC', 'CGTACG'), ('GTACGA', 'TACGAT')]