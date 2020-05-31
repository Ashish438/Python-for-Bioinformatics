# function findGC_pos for finding GC content in reads of fastq file by position

from reading_fastq import read_fastq

def findGC_pos(reads):
	GC = [0] * 127 #since reads in our fastq file are of 127 bases
	Total = [0] * 127
	avg_GC = [0] * 127
	for read in reads:
		for i in range(len(read)):
			if read[i] == "C" or read[i] == "G":
				GC[i] += 1
			Total[i] += 1
	for i in range(len(read)):
		avg_GC[i] = GC[i]/Total[i]
	return avg_GC
		
seqs,quals = read_fastq("path of your fastq file")

GC_content = findGC_pos(seqs)
print(GC_content)
				

##please leave a message if you want a text version of this code or if you face any issues while using the code 
##your personal queries are also invited

	
