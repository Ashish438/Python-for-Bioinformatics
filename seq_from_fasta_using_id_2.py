# Extracting required sequences from a multi fasta file using headers(using Biopython).
# Each required sequences will be extracted in a different output file.

# Input: 
# 1.) Path of multi fasta file from which specific sequences have to be extracted.
# 2.) Path of headers.txt which is a text file containing the headers of our required sequences.

# Output: Different fasta files, each named after the headers of our required sequences.

# Sample Input Files: multi_fasta.fasta, headers.txt
# Sample Output Files: AY179745.fasta, D10845.fasta, D10847.fasta

# multi_fasta_path = r"Enter the path of your multi fasta file"
multi_fasta_path = r"C:\Users\dell\Desktop\NEGENOME_Python\advanced\seq_from_fasta_using_id\multi_fasta.fasta"

# headers_txt_path = r"Enter the path of your headers.txt file"
headers_txt_path = r"C:\Users\dell\Desktop\NEGENOME_Python\advanced\seq_from_fasta_using_id\headers.txt"


# function ExtractSeqFromFasta takes the path of the multi fasta file and headers.txt
# file as input and extracts the required fasta sequence from the fasta files using headers
def ExtractSeqFromFasta(multi_fasta_path,headers_txt_path):
	from pathlib import Path
	from Bio import SeqIO
	
	# converting our string paths to Path objects 
	multi_fasta_path = Path(multi_fasta_path)
	headers_txt_path = Path(headers_txt_path)
 
	# adding each header in our headers.fasta to the headers_list 
	with open(headers_txt_path,"r") as fr2:
		headers_list = fr2.readlines()
		headers_list = [header.rstrip("\n").replace(">","") for header in headers_list]

	# using parse function to extract all sequences from our multi fasta file in all_fasta_records
	all_fasta_records = SeqIO.parse(multi_fasta_path,'fasta')
	
	out_path_list = [] # for storing paths of our output files

	# looping over each fasta record in all_fasta_records
	for fasta_record in all_fasta_records: 
		# checking if the description of our fasta record matches with the header in our header list
		if fasta_record.description in headers_list:
			# generating path of our output files using the record ids
			out_path = multi_fasta_path.parent/fasta_record.id
			# writing fasta record to it's output file	
			SeqIO.write(fasta_record,out_path,"fasta")
			out_path_list.append(out_path)
	
	return 	out_path_list
			
out_path_list = ExtractSeqFromFasta(multi_fasta_path,headers_txt_path)
print("Output files successfully generated at: ", out_path_list)
	
##please leave a message if you face any issues while using the code 
##your personal queries are also invited

	
