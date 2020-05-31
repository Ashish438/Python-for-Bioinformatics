
# counting ATGC in all fasta sequences in a multiple fasta file

fr = open("path of your multiple fasta file","r")
header = ""
seq = ""
for line in fr:
	if ">" in line:
		header = line	
		if seq != "":
			print(seq)
			print("No. of A: ",seq.count("A"))
			print("No. of T: ",seq.count("T"))
			print("No. of G: ",seq.count("G"))
			print("No. of C: ",seq.count("C"))
			seq = ""
		print(header)
		
	else:
		line = line.rstrip("\n")
		seq = seq+line
print(seq)
print("No. of A: ",seq.count("A"))
print("No. of T: ",seq.count("T"))
print("No. of G: ",seq.count("G"))
print("No. of C: ",seq.count("C"))

##please leave a message if you want a text version of this code or if you face any issues while using the code 
##your personal queries are also invited

	
