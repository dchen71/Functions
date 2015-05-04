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
#Suffix(Pattern) = k-1 mer (removed first char)
#firstsymbol(pattern) = 1st char of seq

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
	if len(pattern) == 1:
		return {'A', 'C', 'G', 'T'}
	
	neighborhood = set()
	suffix = pattern[1:len(pattern)]

	suffixneighbors = neighbors(suffix, d)
	for text in suffixneighbors:
		if hammingdist(suffix, text) < d:
			for nucleotide in {'A', 'C', 'G', 'T'}: #undeclared nucleotide variable, called differently?
				suffixneighbors.add(nucleotide * text) #* might actually be product from itertools
		else:
			suffixneighbors.add(nucleotide * text)
	return neighborhood


print(neighbors('ACG',1))