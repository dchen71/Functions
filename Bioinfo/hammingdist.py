'''
Hamming Distance Problem: Compute the Hamming distance between two strings.
     Input: Two strings of equal length.
     Output: The Hamming distance between these strings.
'''

def hammingdist(s1,s2):
	dist = 0
	for i in range(len(s1)):
		if s1[i] != s2[i]:
			dist += 1

	return dist


#Assertion to check function
s1 = 'GGGCCGTTGGT'
s2 = 'GGACCGTTGAC'
assert(hammingdist(s1,s2)) == 3
