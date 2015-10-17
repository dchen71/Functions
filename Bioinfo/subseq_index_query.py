#The following class SubseqIndex is a more general implementation of Index that additionally handles subsequences. It only considers subsequences that take every Nth character: 

from subseq_index import *
from readgenome import *

def query_subseq(p,t,subseq_ind, k):
    occurrences = []
    num_index_hits = 0

    for i in range(len(t) - len(p) + 1):  # loop over alignments
        mismatches = 0
        match = True
        skip = 0
        for j in range(len(p) - k):  # loop over characters
            if skip == 0:
                if i in subseq_ind.query(p[j:]): #Checks if the current index contains subset of the character
                    num_index_hits += 1
                    skip += k
                else:
                    if t[i+j] != p[j]: # compare characters
                        if mismatches < 2:
                            mismatches += 1
                        else:
                            match = False
                            break    
            else:  
                skip -= 1
                
        if match:
            occurrences.append(i)  # all chars matched; record

    return occurrences, num_index_hits

#Tests
t = 'to-morrow and to-morrow and to-morrow creeps in this petty pace'
p = 'to-morrow and to-morrow '
k=8
subseq_ind = SubseqIndex(t, k, 3)
occurrences, num_index_hits = query_subseq(p, t, subseq_ind, k)
assert(occurrences) == [0,14]
assert(num_index_hits) == 6
