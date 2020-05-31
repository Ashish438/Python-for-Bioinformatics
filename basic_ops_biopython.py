
# some basic operations on a sequence using biopython

from Bio.Seq import Seq
my_seq = Seq("AGAACCGGTAGCTGACGT")
print(my_seq)
print(len(my_seq))
print(my_seq[::-1]
print(my_seq[0:2])
print(my_seq.count("A"))
print(my_seq.count("T"))
print(my_seq.count("G"))
print(my_seq.count("C"))
print(my_seq.reverse_complement())
print(my_seq.transcribe())
print(my_seq.translate())

##please leave a message if you want a text version of this code or if you face any issues while using the code 
##your personal queries are also invited

	
