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

#Finds the open reading frames in each DNA sequence in a fasta, 5' to 3' only
def orf(seq):
	orf = {}
	for key, value in sequences.items():
		start = 0
		stop = 3
		kmers = []
		if value.seq.find('ATG', start) != -1:
			start = value.seq.find('ATG', start)
			while(start < len(value)):

				for codon in ('TAA','TAG','TGA'):
					stop_codon = value.seq.find(codon, start)
					if stop_codon != -1:
						if value.seq[start:start + 3] == 'ATG':
							kmer = str(value.seq[start:stop_codon + 3])
							if len(kmer) % 3 == 0:
								kmers.append(kmer)

				start += 1

		orf.setdefault(key, "")
		orf[key] = kmers
	return orf

orf = orf(sequences)
print('')
print('ORF')
print(orf)

#Finds the open reading frames index in each DNA sequence in a fasta, 5' to 3' only
def orf_pos(seq):
	orf_pos = {}
	for key, value in sequences.items():
		start = 0
		stop = 3
		kmers_start = []
		if value.seq.find('ATG', start) != -1:
			start = value.seq.find('ATG', start)
			while(start < len(value)):

				for codon in ('TAA','TAG','TGA'):
					stop_codon = value.seq.find(codon, start)
					if stop_codon != -1:
						if value.seq[start:start + 3] == 'ATG':
							kmer = str(value.seq[start:stop_codon + 3])
							if len(kmer) % 3 == 0:
								kmers_start.append(start)

				start += 1

		orf_pos.setdefault(key, "")
		orf_pos[key] = kmers_start
	return orf_pos

print('')
print('ORF index')
print(orf_pos(sequences))

#Finds the open reading frames kmer lengths in each DNA sequence in a fasta, 5' to 3' only
def orf_length(orf):
	orf_len = {}
	print('ORF')
	print(orf)
	for key in sequences.keys():
		values = orf.get(key)
		kmers_len = []
		for item in values:
			kmers_len.append(len(item))

		orf_len.setdefault(key, "")
		orf_len[key] = kmers_len
	return orf_len

print('')
print('ORF Length')
print(orf_length(orf))

#Finds repeats of length n in the dictionary of values from fasta reads
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

kmers = repeat(6)

#Finds the total number of occurences in a series of fasta strings
def total_kmer(kmers):
	total_kmer = {}
	for i in kmers:
		for key,value in i.items():
			for kmer, counts in value.items():
				total_kmer.setdefault(kmer, 0)
				total_kmer[kmer] += counts
	return total_kmer

total_kmer = total_kmer(kmers)
print(total_kmer)

#Finds the highest occuring number of kmer within the fasta sequences
def highest_kmer(kmers):
	high = 0
	for key,value in kmers.items():
		if value > high:
			high = value
	return high

highest = highest_kmer(total_kmer)
print(highest)

#Finds the most frequently occuring repeat of length n in all sequences
def freq_kmer(kmers):
	high = 0
	for key, value in kmers.items():
		if value > high:
			high = value
	return value

most_freq = freq_kmer(total_kmer)
print('Most Frequent between all sequences: '+ str(most_freq))

#Finds the number of different max occurence of length n kmers 
def diff_max(highest, kmers):
	count = 0
	for i in kmers:
		for key,value in i.items():
			for kmer, counts in value.items():
				if counts == highest:
					count += 1
	return count

print('Most Frequent highest: ' + str(diff_max(highest,kmers)))

#Checks if a kmer is in a kmer list and returns the counts
def kmer_in(kmer, kmers):
	if kmer in kmers:
		return kmers[kmer]
