
# counting headers of a multiple fasta file

fr = open(r"path of your multiple fasta file","r")
count = 0
for line in fr:
	if (">" in line):
		count = count + 1
fr.close()

print("number of headers are: ", count)

##please leave a message if you want a text version of this code or if you face any issues while using the code 
##your personal queries are also invited

	
