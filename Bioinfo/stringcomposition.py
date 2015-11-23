'''
     Input: An integer k and a string Text.
     Output: Compositionk(Text) (the k-mers can be provided in any order).
'''

#Creates all the kmers in a sequence
def stringcomposition(k,text):
	kmers = set()
	for i in range(len(text) - k + 1):
		kmers.add(text[i:i+k])
	return kmers

