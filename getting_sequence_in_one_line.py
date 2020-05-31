
# getting sequences in a fasta file in one line

fr = open("path of single or multiple fasta file","r")
header = ""
seq = ""
for line in fr:
	if ">" in line:
		header = line	
		if seq != "":
			print(seq)
			seq = ""
		print(header)
		
	else:
		line = line.rstrip("\n")
		seq = seq+line
print(seq)
##please leave a message if you want a text version of this code or if you face any issues while using the code 
##your personal queries are also invited

	
