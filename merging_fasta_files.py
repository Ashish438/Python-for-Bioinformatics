# Merging multiple fasta files (any number of fasta files can be merged)

# Input: Path of the Fasta files that have to be merged
# Output: A single fasta file containing sequences from all the individual fasta files
# Sample Input Files: file1.fasta,file2.fasta,file3.fasta
# Sample Output file: merged.fasta

#### Enter path of fasta files within quotes, seperated by commas ####
in_paths = [r"path of 1st fasta file", r"path of second fasta file"... and so on]

# example:
# in_paths = [r"C:\Users\dell\Desktop\NEGENOME_Python\advanced\merging_fasta_files\file1.fasta",
# r"C:\Users\dell\Desktop\NEGENOME_Python\advanced\merging_fasta_files\file2.fasta",
# r"C:\Users\dell\Desktop\NEGENOME_Python\advanced\merging_fasta_files\file3.fasta"]


# function MergeFasta for merging the fasta files
def MergeFasta(in_paths):
	from pathlib import Path
	# generating path for our output file 'merged.fasta', using the path
	# of our first input files
	out_path = Path(in_paths[0]).parent/"merged.fasta"
	
	fw = open(out_path,"w")
	for path in in_paths:
		path = Path(path)
		fr = open(path,"r")
		for line in fr:
			fw.write(line)
		if line != "\n":
			fw.write("\n")
		
	fw.close()
	fr.close()
	
	return out_path

out_path = MergeFasta(in_paths)
print("Output file successfully generated at: ",out_path)
 
##please leave a message if you face any issues while using the code 
##your personal queries are also invited

	
