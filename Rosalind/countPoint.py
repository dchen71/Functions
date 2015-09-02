#Counts the number of point mutations
#(counts number of different characters in same size string)
def countPoint(gen1,gen2):
	points = 0
	for i in range(len(gen1)):
		if gen1[i] != gen2[i]:
			points+= 1

	return points

#Assertion to check the function
gen1 = "GAGCCTACTAACGGGAT"
gen2 = "CATCGTAATGACGGCCT"
assert(countPoint(gen1,gen2)) == 7
