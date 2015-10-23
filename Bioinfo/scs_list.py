#Modifies shortest common substring method which returns a list of candidates

from scs import *

import itertools

def scs_list(ss):
    """ Returns shortest common superstring of given
        strings, which must be the same length """
    shortest_sup = None
    for ssperm in itertools.permutations(ss):
        sup = ssperm[0]  # superstring starts as first string
        for i in range(len(ss)-1):
            # overlap adjacent strings A and B in the permutation
            olen = overlap(ssperm[i], ssperm[i+1], min_length=1)
            # add non-overlapping portion of B to superstring
            sup += ssperm[i+1][olen:]
        if shortest_sup is None or len(sup) < len(min(shortest_sup)):
            if shortest_sup is None:
                shortest_sup = []
                shortest_sup.append(sup)
            else:
                shortest_sup = []
                shortest_sup.append(sup)
        elif len(sup) == len(min(shortest_sup)):
            shortest_sup.append(sup)
    shortest_sup.sort()
    return shortest_sup  # return shortest list

#Tests
strings = ['ABC', 'BCA', 'CAB']
assert(scs(strings)) == 'ABCAB'
assert(scs_list(strings)) == ['ABCAB', 'BCABC', 'CABCA']

strings = ['GAT', 'TAG', 'TCG', 'TGC', 'AAT', 'ATA']
assert(scs(strings)) == 'TCGATGCAATAG'
assert(scs_list(strings)) == ['AATAGATCGTGC','AATAGATGCTCG','AATAGTCGATGC','AATCGATAGTGC','AATGCTCGATAG','TCGAATAGATGC','TCGATAGAATGC','TCGATGCAATAG','TGCAATAGATCG','TGCAATCGATAG']

