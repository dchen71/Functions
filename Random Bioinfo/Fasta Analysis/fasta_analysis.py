#Loads modules from BioPython
from Bio import SeqIO

#Reads the fasta file
fasta = SeqIO.parse("dna.example.fasta", "fasta")

#Converts the fasta file into dictionary entries
sequences = {}
for seq_record in fasta:
	sequences[seq_record.id] = seq_record.seq

#Reads number of fasta records in a file
print("Number of Records : " + str(len(sequences)))

#Finds the length of each seqeunce in a file
for key,value in sequences.items():
	print("Entry: " + key)
	print("Length: " + str(len(value)))

#Finds the open reading frames in each DNA sequence in a fasta

#Finds repeats in a sequence of DNA
