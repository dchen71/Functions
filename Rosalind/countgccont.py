#Counts the percent of GC content in a series of Fasta and return the fasta id with highest content and percentage
#Need to figure out why the incorrect value is returned for gc content
import operator

def countgccont():
	f = open('rosalind_gc.txt', 'r')
	lastkey = ""
	total = 0
	gc = 0
	fastaseq = {}
	#Checks each line
	for line in f:
		#Checks if the line starts as Rosalind
		if line[1:9] == "Rosalind":
			#First time running function
			if total == 0:
				fastaseq[line] = 0
				lastkey = line
			#If if ran before, computes the gc/total
			else:
				fastaseq[lastkey] = gc/total
				gc = 0
				total = 0
				fastaseq[line] = 0
				lastkey = line
		else:
			total += len(line)
			for nuc in line:
				if nuc == 'G' or nuc == 'C':
					gc += 1
	fastaseq[lastkey] = gc/total

	return (max(fastaseq.items(),key=operator.itemgetter(1)))

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