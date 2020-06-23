# Merging multiple fasta files modified(any number of fasta files can be merged)
# This is a simplified version of the previous code 'merging_fasta_files.py'

# Input: Path of the Fasta files that have to be merged
# Output: A single fasta file containing sequences from all the individual fasta files
# Sample Input Files: file1.fasta,file2.fasta,file3.fasta
# Sample Output file: merged.fasta

#### Enter path of fasta files within quotes, seperated by commas ####
in_paths = [r"path of 1st fasta file", r"path of second fasta file"... and so on]

# example:
# in_paths = [r"C:\Users\dell\Desktop\test\file1.fasta",
# r"C:\Users\dell\Desktop\test\file2.fasta",
# r"C:\Users\dell\Desktop\test\file3.fasta"]


# function MergeFasta for merging the fasta files
def MergeFasta(in_paths):
	from pathlib import Path
	# generating path for our output file 'merged.fasta', using the path
	# of our first input files
	out_path = Path(in_paths[0]).parent/"merged.fasta"
	
	with open(out_path,"w") as fw:
		for path in in_paths:
			path = Path(path)
			with open(path,"r") as fr:
				temp = fr.readlines()
				fw.writelines(temp)
				if temp[-1] != "\n":
					fw.write("\n")
					
		
	
	return out_path

out_path = MergeFasta(in_paths)
print("Output file successfully generated at: ",out_path)
 
##please leave a message if you face any issues while using the code 
##your personal queries are also invited

	
