#Builds all possible sequences of k length

import itertools

def sequences(k):
	kmerList = {}
	nuc = 'ATGC'
	seqs = itertools.permutations(nuc)
	seqList = seqs

	for i in seqs:
		kmer = ""
		for begin in range(k):
			kmer += i[begin]
		kmerList[kmer] = 0

	return kmerList

test = sequences(4)

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