#Naive pattern finder with ability to check the pattern and reverse complement of a pattern to string

from reversecomp import *
from naive import *

def naive(p, t):
    occurrences = []
    for i in range(len(t) - len(p) + 1):  # loop over alignments
        match = True
        for j in range(len(p)):  # loop over characters
            if t[i+j] != p[j]:  # compare characters
                match = False
                break
        if match:
            occurrences.append(i)  # all chars matched; record
    return occurrences

def naive_with_rc(p,t):
    occur_for = naive(p,t)
    occur_rev = naive(reverseComplement(p),t)
    occurrences = []
    for i in occur_for:
        if i not in occurrences:
            occurrences.append(i)
    for i in occur_rev:
        if i not in occurrences:
            occurrences.append(i)

    return(occurrences)


#Tests
p = 'CCC'
ten_as = 'AAAAAAAAAA'
t = ten_as + 'CCC' + ten_as + 'GGG' + ten_as
assert(naive_with_rc(p, t)) == [10,23]

p = 'CGCG'
t = ten_as + 'CGCG' + ten_as + 'CGCG' + ten_as
assert(naive_with_rc(p, t)) == [10,24]

