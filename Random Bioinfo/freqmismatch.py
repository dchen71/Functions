'''
Frequent Words with Mismatches Problem: Find the most frequent k-mers with mismatches in a string.
     Input: A string Text as well as integers k and d. (You may assume k ≤ 12 and d ≤ 3.)
     Output: All most frequent k-mers with up to d mismatches in Text.
'''

import itertools

'''
 psuedo better version
 
    FrequentWordsWithMismatches(Text, k, d)
        FrequentPatterns ← an empty set
        for i ← 0 to 4k − 1
            Close(i) ← 0
            FrequencyArray ← 0
        for i ← 0 to |Text| − k
            Neighborhood ← Neighbors(Text(i, k), d)
            for each Pattern from Neighborhood
                index ← PatternToNumber(Pattern)
                Close(index) ← 1
        for i ←0 to 4k − 1
            if Close(i) = 1
                Pattern ← NumberToPattern(i, k)
                FrequencyArray(i) ← ApproximatePatternCount(Text, Pattern, d)
        maxCount ← maximal value in FrequencyArray
        for i ←0 to 4k − 1
            if FrequencyArray(i) = maxCount
                Pattern ← NumberToPattern(i, k)
                add Pattern to the set FrequentPatterns
       return FrequentPatterns 
'''

#Very slow, better off following advice and building after checking the first char
#Probably check chars and build based on d
#Also does not have all possible kmers

#Builds and return a dictionary list of all kmer possibilties for length k
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

#Only checks two equal length and find differences between the two strings
def hammingdist(s1,s2):
	dist = 0
	for i in range(len(s1)):
		if s1[i] != s2[i]:
			dist += 1

	return dist

#Counts the number of times a pattern with d mismatches
def PatternCount(text, pattern, d):
	count = 0
	dist = 0
	i = 0

	#loops through the text and matches pattern character by character for mismatch
	for i in range(len(text)-len(pattern)):
		dist = hammingdist(text[i:i+len(pattern)],pattern)

		if dist <= d:
			count += 1
			dist = 0
		
	return count

#Checks a string for most frequent pattern of k length
def freq_mismatch(text, k,d):
	freqPat = []
	pattern = sequences(k)
	
	#Builds truncated strings along with number of counts in text
	for i in range(len(text) - k):
		kmer = text[i: i + k]
		for key, value in pattern.items():
			if hammingdist(kmer, key) <= d:
				pattern[key] += 1

	highest = max(pattern, key=pattern.get)
	print(highest)

	#Finds highest number value and adds it to a new array
	for key, values in pattern.items():
		if pattern[highest] == values:
			freqPat.append(key)		
	
	answer = ""

	#Builds answer as required by problem
	for i in range(len(freqPat)):
		answer += freqPat[i] + " "
	
	return answer

'''
text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
k = 4
d = 1
#GATG ATGC ATGT
print(freq_mismatch(text,k,d))
'''

text = "CACAGTAGGCGCCGGCACACACAGCCCCGGGCCCCGGGCCGCCCCGGGCCGGCGGCCGCCGGCGCCGGCACACCGGCACAGCCGTACCGGCACAGTAGTACCGGCCGGCCGGCACACCGGCACACCGGGTACACACCGGGGCGCACACACAGGCGGGCGCCGGGCCCCGGGCCGTACCGGGCCGCCGGCGGCCCACAGGCGCCGGCACAGTACCGGCACACACAGTAGCCCACACACAGGCGGGCGGTAGCCGGCGCACACACACACAGTAGGCGCACAGCCGCCCACACACACCGGCCGGCCGGCACAGGCGGGCGGGCGCACACACACCGGCACAGTAGTAGGCGGCCGGCGCACAGCC"
k = 10
d = 2
#GCACACAGAC GCGCACACAC 
print(freq_mismatch(text,k,d))



'''
text = "AAGTTGGTGTTGTTGTTGAAGAGTAGTAGTAGAGTGAGAAAGTTGTTGGTGGTGAGAAGTAGTAGTAAGTTGAGAAGTAGTAAGGTGTTGTTGAAGTTGGTGAGTAAGAAGAGAAAGAGTAGATTGTTGAAGAGTGTGAGTTTGAGAAAGTTGAGAGTGAGTGTGAGTGTGGTGAAGAGTAGTGTGTTGTTGAGTAAGAGTAGAGTGTTGGTGTTGAGAAGTAGAAAGAGATTGAGTTTGAAGTTGAGATTGAAGGTGTTGAAGAGTAGTTTGGTGAGTAGAAGTAGAGTGAGTAGATTGTTGAGTAGTAGTAGTGTGAGAAGTAGAAAGAGTAGTAAGAGTAAGGTGAAGAGATTGGTGAGTGTGAAGTTG"
k = 6
d = 3
print(freq_mismatch(text,k,d))
'''

