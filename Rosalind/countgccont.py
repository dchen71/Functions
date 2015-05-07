#Counts the percent of GC content in a series of Fasta and return the fasta id with highest content and percentage

def countgccont():
	f = open('rosalind_gc.txt', 'r')
	lastkey = ""
	total = 0
	gc = 0
	fastaseq = {}
	print(f.readlines()[0:20])
	#Want to seaprate out files and store rosalind : sequence
	#Need to parse out the \n
	#alt is to scan gc and add to last one but would need a total length counter
	for line in f:
		#Check 1st 8 char for rosalind, != then store it as part of dict
		if line[1:8] == "Rosalind":
			if total == 0:
				fastaseq[line] = 0
				lastkey = line
			else:
				fastaseq[lastkey] = gc/total
				gc = 0
				total = 0
		else:
			total += len(line)
			for nuc in line:
			#Need a way to know it is part of that key then input it
			#fastaseq[lastkey] = line
				if nuc == 'G' or nuc == 'C':
					gc += 1
	
	answer = ""
	for key, value in fastaseq:
		if max(fastaseq) == value:
			answer = key + '\n' + value

	return answer



print(countgccont())