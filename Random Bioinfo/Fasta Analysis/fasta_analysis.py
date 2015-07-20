#Reads multi fasta searches and returns some light information about them

#!/usr/bin/python

#Loads modules from BioPython
from Bio import SeqIO

#Biopython method to read and convert sequence into dictionary
sequences = SeqIO.to_dict(SeqIO.parse("dna.example.fasta", "fasta"))

#Reads number of fasta records in a file
print("Number of Records : " + str(len(sequences)))

#Finds the length of the largest and shortest sequence in the file
length = []
for key,value in sequences.items():
	length.append(len(value))
print("Longest seqeunce: " + str(max(length)))
print("Shortest sequence: " + str(min(length)))

#Finds the open reading frames in each DNA sequence in a fasta
for key,value in sequences.items():
	pass

#Finds repeats of length n in a sequence of DNA
def repeat(n=1):
	fasta_seq = []
	for key, value in sequences.items():
		kmers = {}
		
		for i in range(len(value) - 1):
			kmer = str(value.seq[i:i+n])
			kmers.setdefault(kmer,0)
			kmers[kmer] += 1
		
		entry = {key: kmers}
		fasta_seq.append(entry)
	return fasta_seq

print(repeat(2))