#Builds all possible sequences of k length

import itertools
#combinations does combos based on position in sequence and not the value itself
#needs to start with the other three bases in order to successfully make ther rest

def sequences(k):
	kmerList = {}
	nuc = 'ATGC'
	seqs = itertools.product(nuc,repeat = k)
	seqList = seqs

	for i in seqs:
		kmer = ""
		for begin in range(k):
			kmer += i[begin]
		kmerList[kmer] = 0

	return kmerList

#test out the usage of combinations with replacement


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