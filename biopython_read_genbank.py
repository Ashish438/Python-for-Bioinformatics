
# reading a genbank file having a single sequence using biopython 

from Bio.SeqIO import read
seq_record = SeqIO.read("path of your single genbank file","genbank")
print(seq_record)
print(seq_record.seq)
print(seq_record.id)
print(seq_record.name)
print(seq_record.description)

##please leave a message if you want a text version of this code or if you face any issues while using the code 
##your personal queries are also invited

	

