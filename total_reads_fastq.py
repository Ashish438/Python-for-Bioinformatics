# Finding total number of reads in a fastq file
# Type "python total_reads_fastq.py -i Path of your fastq file" for running the code
# Example: python total_reads_fastq.py -i C:\Users\dell\Desktop\test\sample_fastq.fastq
# Type "python total_reads_fastq.py for help/usage description
# Output: Total number of the reads in a fastq file
# Sample input file: sample_fastq.fastq

import argparse

parser = argparse.ArgumentParser(description="Finding total number of reads in a fastq file, "
                                             "USAGE: python total_reads_fastq.py -i path/to/fastq/file")

parser.add_argument("-i", help = "ENTER FULL PATH OF THE FASTQ FILE")
args = parser.parse_args()
fastq_path = args.i

total_lines = 0
with open(fastq_path,"r") as fr:
    for line in fr:
        total_lines += 1

total_reads = total_lines//4
print(f"Total number of reads in fastq file are {total_reads}")

