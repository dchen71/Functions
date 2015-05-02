#Builds all possible sequences of k length

from itertools import combinations_with_replacement

def sequences(k):
	seqList = {}
#test out the usage of combinations with replacement