#Computes the skew of a string based on number of G and C
# G += 1, C-= 1

def skew(string):
	num = 0
	output = "0 "

	for i in string:
		
		if i == 'C':
			num -= 1
		elif i == 'G':
			num += 1
		output += str(num) + " "

	return output[:-1]

#Assert to check validity
assert(skew("CATGGGCATCGGCCATACGCC")) == '0 -1 -1 -1 0 1 2 1 1 1 0 1 2 1 0 0 0 0 -1 0 -1 -2'
text = "TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT"
assert(skew(text)) == '0 0 0 0 0 1 1 0 0 1 0 -1 0 0 1 1 2 3 2 1 1 1 0 0 -1 0 0 1 1 2 1 1 1 2 2 2 1 2 2 3 4 5 6 5 6 6 6 6 6 5 6 5 6 7 8 8 7 6 7 7 7'