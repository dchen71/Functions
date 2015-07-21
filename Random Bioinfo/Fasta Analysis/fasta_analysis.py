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
def orf(seq):
	#set key as itself, values = orf
	orf = {}
	for key, value in sequences.items():
		start = 0
		stop = 3
		kmers = []
		if value.seq.find('ATG', start) != -1:
			start = value.seq.find('ATG', start)
			while(value.seq.find('ATG', start) != -1):
				start = value.seq.find('ATG', start)
				TAA = value.seq.find('TAA', start)
				TAG = value.seq.find('TAG', start)
				TGA = value.seq.find('TGA', start)
				
				#Logic to determine lowest index for stop codon
				if TAA == -1:
					if TAG == -1 and TGA != -1:
						stop = TGA
					elif TGA == -1 and TAG != -1:
						stop = TAG
					elif TGA == -1 and TAG == -1:
						break;
					else:
						stop = min(TAG,TGA)
				elif TAG == -1:
					if TAA == -1 and TGA != -1:
						stop = TGA
					elif TGA == -1 and TAA != -1:
						stop = TAA
					elif TGA == -1 and TAA == -1:
						break;
					else:
						stop = min(TAA,TGA)
				elif TGA == -1:
					if TAA == -1 and TAG != -1:
						stop = TAG
					elif TAG ==-1 and TAA != -1:
						stop = TAA
					elif TAA == -1 and TAG == -1:
						break;
					else:
						stop = min(TAA,TAG)
				else:
					stop = min(TAA, TAG, TGA)
				stop += 3
				if (stop - start) >= 6:
					kmer = str(value.seq[start:stop])
					kmers.append(kmer)

				start = stop
		orf.setdefault(key, "")
		orf[key] = kmers
	return orf
print(orf(sequences))

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
