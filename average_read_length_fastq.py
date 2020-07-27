# Finding the average length of the reads in a fastq file using biopython

# Type "python average_read_length_fastq.py -i Path of your fastq file" for running the code
# Example: python average_read_length_fastq.py -i C:\Users\dell\Desktop\test\sample_fastq.fastq

# Type "python average_read_length_fastq.py -h" for help/usage description

# Output: Average length of the reads in a fastq file

# Sample input file: sample_fastq.fastq

from Bio import SeqIO
import argparse

parser=argparse.ArgumentParser(description="Finding the average length of the reads in a fastq file , USAGE: python average_read_length_fastq.py -i path/to/fastq/file ")
parser.add_argument("-i", help="ENTER FULL PATH OF THE FASTQ FILE")
args = parser.parse_args()

fastq_path = args.i
fastq_records = SeqIO.parse(fastq_path,"fastq")
total_read_count = 0
total_read_length = 0
for fastq_record in fastq_records:
	total_read_count += 1
	total_read_length += len(fastq_record.seq)
	
average_read_length = total_read_length//total_read_count
print("Average read length in fastq file is: ",average_read_length)

## please leave a message if you face any issues while using the code 
## your personal queries are also invited