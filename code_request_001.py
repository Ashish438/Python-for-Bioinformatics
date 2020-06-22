#### The following code is the solution of a personal code request(code_request_001)####

# Performing cutadapt on a set of fastq files
# This code will perform cutadapt for both single and paired end files, taking one file at a time
# The cutadapt command used is this code is "cutadapt -j 1  --error-rate=0.1 --times=1 --overlap=3 --minimum-length=20 --quality-cutoff=20 -o " + output_file + " " + input_file"
# Input: Path of fastq files(both single or paired end)
# Output: Trimmed output files(generated after cutadapt) of the respective input files

#### Enter the path of your input fastq files ####
input_file_list = ["path of file1","path of file2"...]	
# e.g: input_file_list = ["C:\Users\dell\Desktop\file1.fatsq","C:\Users\dell\Desktop\file2.fatsq"...]
#### Enter the path of your input fastq files ####

from subprocess import check_output
import os

# function for fetching systems cutadapt path
def fetch_cutadapt_path():
	cutadapt_path_comm = "which cutadapt".split(" ")
	out = check_output(cutadapt_path_comm)
	cutadapt_comm_path = str(out, 'UTF8').strip("\n") + " "
	return cutadapt_comm_path

# cutadapt function for running the cutadapt command on each file 
def cutadapt(file,cutadapt_comm_path):
	filename = file.split("/")[-1]
	# generating the output file path from input file path
	out_file_path = file.strip(".fq")+"_trimmed"+".fq"
	# generating the complete cutadapt command
	cutadapt_comm = cutadapt_comm_path + "-j 1  --error-rate=0.1 --times=1 --overlap=3 --minimum-length=20 --quality-cutoff=20 -o " + out_file_path + " " + file
	# running the cutadapt command
	os.system(cutadapt_comm)
	print("cutadapt successful for {}, output generated at:  {}".format(filename,out_file_path))

# main function for passing each file to the cutadapt function
def main(input_file_list):
	cutadapt_comm_path = fetch_cutadapt_path()
	# looping over each file path in input_file_list 
	for file in input_file_list:
		# calling cutadapt function for each file
		cutadapt(file,cutadapt_comm_path)
	
# calling main function
main(input_file_list)
print("cutadapt successfull for all input files")

##please leave a message if you face any issues while using the code 
