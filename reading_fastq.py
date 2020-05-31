# function read_fastq for fetching reads and phred scores in fastq file in two seperate lists

def read_fastq(input):
	sequences = []
	qualities = []
	fr  = open(input,"r")
	while(True):
		fr.readline()
		seq = fr.readline()
		fr.readline()
		qual = fr.readline()
		if len(seq) == 0:
			break
		sequences.append(seq)
		qualities.append(qual)
	return sequences,qualities

seqs,quals = read_fastq("path of your fastq file")
print(seqs[:5])
print(quals[:5])

##please leave a message if you want a text version of this code or if you face any issues while using the code 
##your personal queries are also invited

	
