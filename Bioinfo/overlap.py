'''
Input: A collection Patterns of k-mers.
Output: The overlap graph Overlap(Patterns), in the form of an adjacency list.
'''

#Creates a overlap graph for a series of kmers
def overlap(patterns):
	overlapping = []
	for kmer in kmers:
		for test in kmers:
			if kmer != test:
				if kmer[1:len(kmer)] == test[0:len(test) - 1]:
					overlapping.append(kmer + " -> " + test)

	return overlapping