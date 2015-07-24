#Counts the number of times a pattern is detected

def PatternCount(text, pattern):
	count = 0
	correct = 0

	#loops through the text and matches pattern character by character
	for i in range(len(text)-len(pattern)):
		for j in range(len(pattern)):
			if(text[j + i] == pattern[j]):
				correct += 1
			
		if correct == len(pattern):
			count += 1
			correct = 0
			i += len(pattern) - 1
		else:
			correct = 0
		
	return count


#Combines parts of array and return full length
def combine(text, start, end):
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
def FrequentWords(text, k):
	freqPat = []
	pattern = []
	count = []
	
	#Builds truncated strings along with number of counts in text
	for i in range(len(text) - k):
		pattern.append(combine(text,i,k + i))
		count.append(PatternCount(text, pattern[i]))

	maxCount = len(count)
	highest = count[0]

	#Finds highest number value
	for i in (range(maxCount)):
		if highest < count[i]:
			highest = count[i]
	
	#Builds the most frequent k-mer
	for i in range(maxCount):	
		if(count[i] == highest):
			if(freqPat.count(pattern[i]) == 0):
				freqPat.append(pattern[i])
	
	return freqPat

'''
text = "ACTGACTCCCACCCC"
k = 3
#ACT,CCC
print(FrequentWords(text, k))

text = "  ACGTTGCATGTCGCATGATGCATGAGAGCT"
k=4
#CATG GCAT
print(FrequentWords(text, k))
'''

text = "ATACTGTGCTCACAGGAGACGCCTGACATTGAAGTCACAGGAGCTTCCAACTTCACAGGAGACGCCTGGACGCCTGATACTGTGCTCACAGGAACATTGAAGGCTTCCAACTATACTGTGCGCTTCCAACTATACTGTGCATACTGTGCACATTGAAGGCTTCCAACTTCACAGGATCACAGGAGACGCCTGTCACAGGAACATTGAAGGCTTCCAACTGCTTCCAACTGACGCCTGACATTGAAGGCTTCCAACTACATTGAAGACATTGAAGTCACAGGAGCTTCCAACTACATTGAAGTCACAGGAGCTTCCAACTACATTGAAGATACTGTGCACATTGAAGACATTGAAGGACGCCTGACATTGAAGGACGCCTGGCTTCCAACTATACTGTGCTCACAGGAATACTGTGCATACTGTGCACATTGAAGGACGCCTGATACTGTGCGACGCCTGACATTGAAGACATTGAAGACATTGAAGTCACAGGAATACTGTGCGCTTCCAACTGACGCCTGACATTGAAGATACTGTGCTCACAGGAACATTGAAGGCTTCCAACTATACTGTGCGACGCCTGGACGCCTGTCACAGGAGCTTCCAACTGCTTCCAACTTCACAGGAACATTGAAGTCACAGGAATACTGTGCGACGCCTGGCTTCCAACTTCACAGGAGACGCCTGACATTGAAGACATTGAAGGCTTCCAACTACATTGAAGACATTGAAGACATTGAAGACATTGAAGATACTGTGCTCACAGGATCACAGGATCACAGGAGCTTCCAACTGACGCCTGTCACAGGAACATTGAAGGCTTCCAACTATACTGTGCGACGCCTGGCTTCCAACTACATTGAAGGCTTCCAACTGCTTCCAACTACATTGAAGTCACAGGAATACTGTGCACATTGAAGGCTTCCAACTATACTGTGCGCTTCCAACTGCTTCCAACTGCTTCCAACTACATTGAAG"
k = 12
print(FrequentWords(text, k))

'''
#cat
print(combine("catdog",0,3))
#k
print(combine("chicken",4,5))
'''