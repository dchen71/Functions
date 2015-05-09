#Counts the percent of GC content in a series of Fasta and return the fasta id with highest content and percentage
#Need to figure out why the incorrect value is returned for gc content, might have something to do with gc since length should be corret now
import operator

def countgccont():
	f = open('rosalind_gc.txt', 'r')
	lastkey = ""
	total = 0
	gc = 0
	fastaseq = {}
	
	#Checks each line
	for line in f:
		print(line)
		#Checks if the line starts as Rosalind
		if line[1:9] == "Rosalind":
			#First time running function
			if total == 0:
				fastaseq[line[1:len(line) - 1]] = 0
				lastkey = line[1:len(line) - 1]
			#If if ran before, computes the gc/total
			else:
				fastaseq[lastkey] = gc/(total) * 100
				gc = 0
				total = 0
				fastaseq[line] = 0
				lastkey = line[1:len(line) - 1]
		else:
			total += len(line) - 1 #each /n cuonts as a space and at end of each line
			for nuc in line:
				if nuc == 'G' or nuc == 'C':
					gc += 1
	fastaseq[lastkey] = gc/(total + 1) * 100 #total+1 cause last line doesnt have /n and this here cause dont compute at end of loop

	return (max(fastaseq.items(),key=operator.itemgetter(1))) #not formated but highest value

'''
>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT

#Rosalind_0808
60.919540
'''

print(countgccont())