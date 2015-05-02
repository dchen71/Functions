#Builds all possible sequences of k length

from itertools import combinations_with_replacement


def sequences(k):
	seqList = {}
	nuc = 'ATGC'
	seqs = combinations_with_replacement(nuc,k)

	for i in seqs:
		kmer = ""
		for begin in range(k):
			kmer += i[begin]
		seqList[kmer] = 0

	return seqList

#test out the usage of combinations with replacement


test = sequences(2)

for key, value in test.items():
	print(key)

'''
test  = combinations_with_replacement('ATGC',2)
fix = []
for i in test:
	print(i[0:len(i)])
	fix.append(i[0] + i[1])

for i in fix:
	print(i)
'''