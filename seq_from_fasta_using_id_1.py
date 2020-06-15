# Extracting sequences of our choice from a multi fasta file using headers 
# All the required sequences will be extracted in a single output file

# Input: 
# 1.) Path of multi fasta file from which specific sequences have to be extracted
# 2.) Path of headers.txt which is a text file containing the headers of our required sequences
# Output: A fasta file named as output.fasta, containing the sequences of our choice
# Sample Input Files: multi_fasta.fasta, headers.txt
# Sample Output File: output.fasta

#### Enter the path of required files ####
multi_fasta_path = "Enter the path of your multi fasta file"
# e.g: multi_fasta_path = r"C:\Users\dell\Desktop\NEGENOME_Python\advanced\seq_from_fasta_using_id\multi_fasta.fasta"

headers_txt_path = "Enter the path of your headers.txt file"
# e.g: headers_txt_path = r"C:\Users\dell\Desktop\NEGENOME_Python\advanced\seq_from_fasta_using_id\headers.txt"
#### Enter the path of required files ####

# function ExtractSeqFromFasta takes the path of the multi fasta file and headers.txt
# file as input and extracts the required fasta sequence from the fasta files using headers
def ExtractSeqFromFasta(multi_fasta_path,headers_txt_path):
	from pathlib import Path

	multi_fasta_path = Path(multi_fasta_path)
	headers_txt_path = Path(headers_txt_path)
	out_path = multi_fasta_path.parent/"output.fasta"

	headers_list = []

	fr1 = open(multi_fasta_path,"r")  
	fr2 = open(headers_txt_path,"r")
	fw = open(out_path,"w") 

	# looping over each line in our headers.fasta and appending each header
	# to the headers_list 
	for line in fr2:
		line = line.strip("\n")
		headers_list.append(line)

	# seq stores the sequence for our required headers 
	seq = ""
	
	# looping over each line in our multi fasta file
	for line in fr1:
		line = line.strip("\n") # removing "\n" from each line
		if ">" in line:
			count = 0
			if seq != "":		
				# writing the extracted sequence for each required
				# to the output file
				fw.write(seq+"\n\n") 
				seq = ""
		
		# looping over each header in the headers_list
		for header in headers_list:
				# this if condition will be true when the header in
				# our headers_list matches with the header in our
				# multi fasta file
				if line == header:
					count += 1
					headers_list.remove(header)
					line += "\n"
					break
		
		if count == 1:
			if ">" in line:
				# writing only the required header line to the output file  
				fw.write(line)
			else:
				# generating the required fasta sequence
				seq += line
			
	
	fr1.close()
	fr2.close()
	fw.close()
	
	return out_path
	
out_path = ExtractSeqFromFasta(multi_fasta_path,headers_txt_path)
print("Output file successfully generated at: ", out_path)
	
##please leave a message if you face any issues while using the code 
##your personal queries are also invited

	
