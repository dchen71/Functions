'''
Frequent Words with Mismatches Problem: Find the most frequent k-mers with mismatches in a string.
     Input: A string Text as well as integers k and d. (You may assume k ≤ 12 and d ≤ 3.)
     Output: All most frequent k-mers with up to d mismatches in Text.
'''

#Only checks two equal length and find differences between the two strings
def hammingdist(s1,s2):
	dist = 0
	for i in range(len(s1)):
		if s1[i] != s2[i]:
			dist += 1

	return dist

def freq_mismatch(text, k ,d):
	kmers = {}
	num = 0
	answer = ""

	#Builds each kmer to check
	for i in range(len(text) - k + 1):
		kmer = text[i: i+k]

		num = 0
		kmers.setdefault(kmer,[])
		for j in range(len(text) - k + 1):
			kmers[kmer] = num

			#Finds the hamming distance between a string and subset of text
			if hammingdist(kmer, text[j: j+k]) <= d:
				num += 1
				kmers[kmer] = num
	print(kmers)
	#Finds the highest appearing kmer and returns the string answer
	for key,value in kmers.items():
		if max(kmers.values()) == value:
			answer += key + " "
	print(max(kmers.values()))

	return answer

'''
text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
k = 4
d = 1
#GATG ATGC ATGT
print(freq_mismatch(text,k,d))
'''


#Has errors
text = "CACAGTAGGCGCCGGCACACACAGCCCCGGGCCCCGGGCCGCCCCGGGCCGGCGGCCGCCGGCGCCGGCACACCGGCACAGCCGTACCGGCACAGTAGTACCGGCCGGCCGGCACACCGGCACACCGGGTACACACCGGGGCGCACACACAGGCGGGCGCCGGGCCCCGGGCCGTACCGGGCCGCCGGCGGCCCACAGGCGCCGGCACAGTACCGGCACACACAGTAGCCCACACACAGGCGGGCGGTAGCCGGCGCACACACACACAGTAGGCGCACAGCCGCCCACACACACCGGCCGGCCGGCACAGGCGGGCGGGCGCACACACACCGGCACAGTAGTAGGCGGCCGGCGCACAGCC"
k = 10
d = 2
#GCACACAGAC GCGCACACAC 
#GCACACAGAC doesn't appear to be in the text though?
print(freq_mismatch(text,k,d))


text = "AATCAAAAAAGAGTTTAGAGTAAAATAAATAATTAGAGTGAGTTTAATAAATAAGAGTGAGTATAAATAATTAATAAGAGTGAGTATAAGAGTAATCTTAAAAGAGTAATCAAAAAATTAAATCATAATTAGAGTGAGTGAGTGAGTAAAATAAGAGTGAGTATAAGAGTGAGTTTAAATCGAGTAATCTTAATAAAAAGAGTTTATTAAATCAATCGAGTATAAATAAATAATTATTAAATCATAATTAAATCTTAAATCAAATTATTAATAAGAGTGAGTAATCGAGTTTAATAATTAATAAAAATTAAATCATAAAAATTAAAAGAGT"
k = 5
d = 3
print(freq_mismatch(text,k,d))
