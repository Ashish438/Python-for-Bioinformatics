
# program to find the reverse complement of a dna sequence

str1 = "ATCGATCGATCGATCG"
complement = ""
for i in range(len(str1)):
	if (str1[i] == "A"):
		complement += "T"
	elif (str1[i] == "G"):
		complement += "C"
	elif (str1[i] == "C"):
		complement += "G"
	elif (str1[i] == "T"):
		complement += "A"
rev_complement = complement[::-1]
print(rev_complement)

##please leave a message if you want a text version of this code or if you face any issues while using the code 
##your personal queries are also invited

	
