#Counts anbd returns the number of bases in a sequence
def countBase(seq):
	numA = 0
	numT = 0
	numC = 0
	numG = 0

	for i in range(len(seq)):
		if seq[i] == 'A':
			numA += 1
		elif seq[i] == 'T':
			numT += 1
		elif seq[i] == 'C':
			numC += 1
		elif seq[i] == 'G':
			numG += 1

	return(str(numA) + " " + str(numC) + " " + str(numG) + " " + str(numT))

text = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
#20 12 17 21
print(countBase(text))

text = "AGCTGGTCCAACGGGAACAGGAAAACTGGACGCTGGTAAGACATACTAAAAGCATATGCATGGACGTGTTTCCAAGTTGGGGTGTCGTAAAGTTCATGTATACCACATACTACACCGCTCCAGAGACTGGCATGGATTAAACGCATCAATGTTTGTGGGGGGGGTCATGTACCTTGATATCCGTCCCACAGGCAGTGCTATGGGTAGAAAATCACTGACACGTATCTATAGCGCCTGCGCTTACCTTGATAGCGTGTCTATTGTTTTACTTTGACACTCGGGCGAGCATCTGGAGTGCCACGTCACTAGCATAATGCTCCAATGGACACTACGCGAGGGATAACCTGACATCGTGGTTTTAAATTGTCGTCGTAAGTATTGCTCAGAGAAACCAGCCTCCAAAGTTTTGAGCGTTATGAGGCATGGCCTTTAAGACATTAGTAGCCTCCAAGGGCTGTTAAGATATATCACCTAGGCAGTGAGGAGGTCAAATCTCCCCCTCTCTTCTGTTAGGATCACACCCATAGACCCACACCATACGGACATGCTTGTCACGCCTAGATGACGATAAGCGAGATGTACTTGGTGCCGCGTAGGTCTTGAGCGTAATTTATTACCATAGTGTAAAAAGTATGGCAGATCTACTAAATCCTGCCGGGTCGACGCGAGCGCAAGACAGAAAAACTGTAAACTGAGGCTTGTGTCCGACTCTCGCACCCTTCCAGTTGTTGGAACCGTGCGTCGCGGAGAGGCTCTTTCGAGTGCCCACTAGTATAAGACCTCTTGTCCGTTGGATCTTAGCGGCATATTCGATGTGGATATGTATCTGTCCCCACGGGCCACAATT"
#218 200 211 218
print(countBase(text))