'''
Input: A sequence of k-mers Pattern1, … ,Patternn such that the last k - 1 symbols of Patterni are
           equal to the first k-1 symbols of Patterni+1 for 1 ≤ i ≤ n-1.
Output: A string Text of length k+n-1 such that the i-th k-mer in Text is equal to Patterni  (for 1 ≤ i ≤ n).
'''

#Creates a genome path from a series of kmers
def genomepath(kmers):
	assembled = kmers.pop(0)

	for kmer in kmers:
		assembled = assembled + kmer[len(kmer) - 1]

	return assembled

kmers = ["ACCGA", "CCGAA", "CGAAG" ,"GAAGC", "AAGCT"]
assert(genomepath(kmers)) == "ACCGAAGCT"