#### code_request_002 ####

# Finding mean of normalised methylation rate of gene parts using pandas
# Our input file is a TSV(tab delimited format) containing list of gene parts with their normalised methylation rate
# Input: Path of the input TSV file 
# Output: TSV file containing list of gene parts with their mean normalised methylation rate
# Sample input file: bismark.txt
# Sample output file: output_bismark.txt

# Column indexes and headers of our input file:  
# column 0 -> chromosome number
# column 1 -> start coordinate
# column 2 -> end coordinate
# column 3 -> methylation rate
# column 4 -> gene_part (e.g NR_039983_6 refers to the 6th part of the gene)

# import pathlib and pandas
import pandas as pd
from pathlib import Path

in_path = r"Enter the path of your input tab delimited file"
# e.g: in_path = r"C:\Users\dell\Desktop\code_request_002\bismark.txt"

in_path = Path(in_path)
in_filename = in_path.parts[-1]
out_filename = "output_"+in_filename
out_path = in_path.parent/out_filename # generating path for our output file

# reading our TSV file as a dataframe 'df'
df = pd.read_csv(in_path,sep="\t",header = None)

# initialising empty lists for each of our columns in the output file
mean_list = []
index1_list = []
index2_list = []
chr_list = []

# extracting unique gene parts from our dataframe(column 4) into a series
gene_parts = df[4].unique()

# converting series of unique gene parts to gene_parts list
gene_parts = gene_parts.tolist()

# looping over each gene part in our gene_parts list
for gene_part in gene_parts:
	# extracting the column region having methylation rate of a specific gene part
	working_col = df[3][df[4]==gene_part]
	# extracting the starting and ending coordinates of a specific gene part
	index1 = df[1][df[4]==gene_part].min()
	index2 = df[1][df[4]==gene_part].max()
	# extracting the chr of a specific gene part
	chr = df[0][df[4]==gene_part].reset_index(drop = True)[0]
	
	# appending the mean of the methylation rate of a specific gene part to mean_list
	mean_list.append(working_col.mean())
	# appending other extracted values of a specific gene part to their respective lists
	index1_list.append(index1)
	index2_list.append(index2)
	chr_list.append(chr)

# creating the output dataframe 'df_out' using chr_list,index1_list,index2_list,mean_list,gene_parts
df_out = pd.DataFrame(list(zip(chr_list,index1_list,index2_list,mean_list,gene_parts)))

# writing the output dataframe 'df_out' as tab delimited values to our output file
df_out.to_csv(out_path,sep = "\t",index = False,header = False)

##please leave a message if you face any issues while using the code 
	