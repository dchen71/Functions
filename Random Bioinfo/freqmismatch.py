'''
Frequent Words with Mismatches Problem: Find the most frequent k-mers with mismatches in a string.
     Input: A string Text as well as integers k and d. (You may assume k ≤ 12 and d ≤ 3.)
     Output: All most frequent k-mers with up to d mismatches in Text.
'''

from itertools import combinations_with_replacement
#Need to figure out how to do combinations using itertools then for now brute force it
#k will be up to 12bp long
#k will have d up to 3 wrong whereever
#loop through
#alt is towe suggest you use a window of length k to slide through Text and, for any given k-window, increment all kmers in neighbors(window,d).

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

'''
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


#Builds the kmer possibilties
#Needs to set this up so it can make all the kmers starting from 1st char
def combine(text, start, k):
	word = []
	
	for i in range(abs(start - end)):
		word.append(text[start + i])

	length = len(word)
	answer = ""
	while length != 0:
		answer += word.pop(0)
		length -= 1

	return answer

#Checks a string for most frequent pattern of k length
def freq_mismatch(text, k,d):
	freqPat = []
	pattern = {}
	count = []
	
	#Builds truncated strings along with number of counts in text
	for i in range(len(text) - k):
		pattern[(combine(text,i,k)] = 0 #this part needs editing, adjust it so it checks all 4 baess to k
		count.append(PatternCount(text, pattern[i],d))

	maxCount = len(count)
	highest = count[0]

	#Finds highest number value
	for key, values in pattern.items():
		if max(pattern) == values:
			freqPat.append(key)		
	
	#Builds the most frequent k-mer in the answer format specified
	for i in range(maxCount):	
		if(count[i] == highest):
			if(freqPat.count(pattern[i]) == 0):
				freqPat.append(pattern[i])
	
	for i in range(len(pattern)):
		print(pattern[i] + ': ' + str(count[i])) 
	

	return freqPat
'''

'''
#Look into whether or not it also shows the mismatch version of it or not
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
	print(max(kmers.values()))
	for key,value in kmers.items():
		if max(kmers.values()) == value:
			answer += key + " "
			


	return answer
'''

'''
text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
k = 4
d = 1
#GATG ATGC ATGT
print(freq_mismatch(text,k,d))
'''

'''
#Has errors
text = "CACAGTAGGCGCCGGCACACACAGCCCCGGGCCCCGGGCCGCCCCGGGCCGGCGGCCGCCGGCGCCGGCACACCGGCACAGCCGTACCGGCACAGTAGTACCGGCCGGCCGGCACACCGGCACACCGGGTACACACCGGGGCGCACACACAGGCGGGCGCCGGGCCCCGGGCCGTACCGGGCCGCCGGCGGCCCACAGGCGCCGGCACAGTACCGGCACACACAGTAGCCCACACACAGGCGGGCGGTAGCCGGCGCACACACACACAGTAGGCGCACAGCCGCCCACACACACCGGCCGGCCGGCACAGGCGGGCGGGCGCACACACACCGGCACAGTAGTAGGCGGCCGGCGCACAGCC"
k = 10
d = 2
#GCACACAGAC GCGCACACAC 
#GCACACAGAC doesn't appear to be in the text though?
print(freq_mismatch(text,k,d))
'''


'''
text = "AAGTTGGTGTTGTTGTTGAAGAGTAGTAGTAGAGTGAGAAAGTTGTTGGTGGTGAGAAGTAGTAGTAAGTTGAGAAGTAGTAAGGTGTTGTTGAAGTTGGTGAGTAAGAAGAGAAAGAGTAGATTGTTGAAGAGTGTGAGTTTGAGAAAGTTGAGAGTGAGTGTGAGTGTGGTGAAGAGTAGTGTGTTGTTGAGTAAGAGTAGAGTGTTGGTGTTGAGAAGTAGAAAGAGATTGAGTTTGAAGTTGAGATTGAAGGTGTTGAAGAGTAGTTTGGTGAGTAGAAGTAGAGTGAGTAGATTGTTGAGTAGTAGTAGTGTGAGAAGTAGAAAGAGTAGTAAGAGTAAGGTGAAGAGATTGGTGAGTGTGAAGTTG"
k = 6
d = 3
print(freq_mismatch(text,k,d))
'''

print(combinations_with_replacement('ABCD',3))