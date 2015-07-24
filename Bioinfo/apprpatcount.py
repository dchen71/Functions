'''
	Cpimts the approximate number of patterns that appears less or equal than d times
    ApproximatePatternCount(Text, Pattern, d)
        count ← 0
        for i ← 0 to |Text| − |Pattern|
            Pattern′ ← Text(i , |Pattern|)
            if HammingDistance(Pattern, Pattern′) ≤ d
                count ← count + 1
        return count
'''

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

text = "TTTAGAGCCTTCAGAGG"
pattern = "GAGG"
d = 2
#4
print(appratcount(text,pattern,d))

text = "CAGTTTACAAGCTCATGATTATTTCTCCGGCACCGCAAGAAATCTCTGTGTACCACTGATATTAGGCTTTAGAACGTTCAGCGGTTTTATTCCCTCCCTAGAGATATACGTTTCAGGTTTTGTTCTCCACGAACAACTGATACATAAAAATGACACACATCCATTGCGGGTGGTGCAGGCTACAAATGTGCGCTGTTAAAAAAGGAGGGGCAATCAGGAGCGAGGCCTAGCCAAGGTAGTAGCGTATGTAATCGAACCCCACGATACTTTCCGCTCATAAGCGTGTTGTCGGTTCTGACGGTTAGCCCTGCTTAGCTTTAAATCTCTAATAAGGCTTTGTGTTCGCCATACTATCGTCCACATGAACTCCGGCCCAATGTAG"
pattern = "TATTC"
d = 2
#4
print(appratcount(text,pattern,d))
