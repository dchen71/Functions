'''
   Creates the next nucleotide version of mismatched basepairs

    Neighbors(Pattern, d)
        if d = 0
            return {Pattern}
        if |Pattern| = 1 
            return {A, C, G, T}
        Neighborhood ← an empty set
        SuffixNeighbors ← Neighbors(Suffix(Pattern), d)
        for each string Text from SuffixNeighbors
            if HammingDistance(Suffix(Pattern), Text) < d
                for each nucleotide x
                    add x • Text to Neighborhood
            else
                add FirstSymbol(Pattern) • Text to Neighborhood
        return Neighborhood
'''


#Only checks two equal length and find differences between the two strings
def hammingdist(s1,s2):
	dist = 0
	for i in range(len(s1)):
		if s1[i] != s2[i]:
			dist += 1

	return dist

#Creates the next nucleotide version of mismatched basepairs
def neighbors(pattern, d):
	if d == 0:
		return pattern
	if #|pattern| = 1
		return {'A', 'C', 'G', 'T'}
	neighborhood = set()
	suffixneighbors = neighbors(#Suffix(pattern, d))
	for text in suffixneighbors:
		if hammingdist(#Suffix(pattern), text) < d:
			for nucleotide in {'A', 'C', 'G', 'T'}:
				suffixneighbors.add(nucleotide * text)
		else:
			suffixneighbors.add(nucleotide * text)
	return neighborhood

