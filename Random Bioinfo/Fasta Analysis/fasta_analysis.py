from Bio import SeqIO

for seq_record in SeqIO.parse("dna.example.fasta", "fasta"):
	print(seq_record.id)
	print(repr(seq_record.seq))
	print(len(seq_record))

#Reads number of fasta records in a file

test = {'cat': 'dog'}
print(test['cat'])


#Finds the length of each seqeunce in a file

#Finds the open reading frames in each DNA sequence in a fasta

#Finds repeats in a sequence of DNA
