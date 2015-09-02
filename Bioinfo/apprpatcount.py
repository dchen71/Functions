#Counts the approximate number of patterns that appears less or equal than d times

def hammingdist(s1,s2):
	dist = 0
	for i in range(len(s1)):
		if s1[i] != s2[i]:
			dist += 1
			
	return dist

def appratcount(text,pattern,d):
	count = 0
	for i in range(len(text) - len(pattern) + 1):
		pattern2 = text[i:i + len(pattern)]
		if hammingdist(pattern, pattern2) <= d:
			count+= 1
	return count

#Assertions to check function
text = "TTTAGAGCCTTCAGAGG"
pattern = "GAGG"
d = 2
#4
assert(appratcount(text,pattern,d)) == 4
