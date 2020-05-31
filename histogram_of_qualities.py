
# function create_hist for creating histogram for qualities of the reads in your fastq file 
# function visualise for visualizing the same using matplotlib 

from QtoPhred import phredtoQ
from reading_fastq import read_fastq

def create_hist(qualities):	
	hist = [0] * 50
	for seq in qualities:
		for phred_score in seq:
			q = phredtoQ(phred_score)
			hist[q] += 1
		
	return hist

seqs,quals = read_fastq("path of your fastq file")

h = create_hist(quals)
print(h)

def visualise(hist):
	import matplotlib.pyplot as plt
	plt.bar(range(len(hist)),hist)
	plt.show()

visualise(h)

##please leave a message if you want a text version of this code or if you face any issues while using the code 
##your personal queries are also invited

	
