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

#Switch function to search stop codons backwards
def orf(seq):
	orf = {}
	orf_length = {}
	orf_pos = {}
	for key, value in sequences.items():
		start = 0
		stop = 3
		kmers = []
		kmers_length = []
		kmers_start = []
		if value.seq.find('ATG', start) != -1:
			start = value.seq.find('ATG', start)
			while(start < len(value)):

				TAA = value.seq.find('TAA', start)
				TAG = value.seq.find('TAG', start)
				TGA = value.seq.find('TGA', start)
				
				if TAA != -1:
					if value.seq[start:start + 3] == 'ATG':
						kmer = str(value.seq[start:TAA + 3])
						if len(kmer) % 3 == 0:
							kmers.append(kmer)
							kmers_start.append(start)
							kmers_length.append(len(kmer))
				if TAG != -1:
					if value.seq[start:start + 3] == 'ATG':
						kmer = str(value.seq[start:TAG + 3])
						if len(kmer) % 3 == 0:
							kmers.append(kmer)
							kmers_start.append(start)
							kmers_length.append(len(kmer))
				if TGA != -1:
					if value.seq[start:start + 3] == 'ATG':
						kmer = str(value.seq[start:TGA + 3])
						if len(kmer) % 3 == 0:
							kmers.append(kmer)
							kmers_start.append(start)
							kmers_length.append(len(kmer))
				start += 1

		orf_length.setdefault(key, "")
		orf_pos.setdefault(key, "")
		orf.setdefault(key, "")
		orf[key] = kmers
		orf_length[key] = kmers_length
		orf_pos[key] = kmers_start
	return orf

orf = orf(sequences)
print(orf)

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
