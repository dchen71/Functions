#Counts the percent of GC content in a series of Fasta and return the fasta id with highest content and percentage

def countgccont():
	f = open('rosalind_gc.txt', 'r')
	lastkey = ""
	fastaseq = {}
	print(f.readlines()[0:20])
	#Want to seaprate out files and store rosalind : sequence
	#Need to parse out the \n
	for line in f:
		#Check 1st 8 char for rosalind, != then store it as part of dict
		if line[0:7] == "Rosalind":
			#Make a blank key for dict
			#lastkey = whatever this line is
		else:
			#Need a way to know it is part of that key then input it
			#fastaseq[lastkey] = line



print(countgccont())