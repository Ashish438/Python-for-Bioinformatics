# Removing all sequences(contigs) less than a particular length from a fasta file derived from metagenomic data
# Here the length of the sequences to be removed is taken as 300 bp
# Type "python remove_seq.py -i Path/of/your/fasta/file -l Cut off length of the sequences to be removed
# - o Output file name with extension" for running the code
# Example: python remove_seq.py -i C:\Users\dell\PycharmProject\fb_page\metagenomic.fasta -l 300
# -o metagenomic_out.fasta
# Type "python remove_seq.py -h" for help/usage description
# Output: Fasta file with only those sequences which are greater than or equal to the specified length(e.g. 300)
# Sample input file: metagenomic.fasta
# Sample output file: metagenomic_out.fasta

import argparse
from pathlib import Path
from Bio import SeqIO

parser = argparse.ArgumentParser(description="Removing all sequences(contigs) less than a particular length from a fasta file",
                                usage= "remove_seq.py -i path/to/fasta/file -l Cut off length of the sequences to be removed -o Output filename with extension")

parser.add_argument("-i", help="ENTER FULL PATH OF THE FASTA FILE")
parser.add_argument("-l", help="ENTER CUT OFF LENGTH OF THE SEQUENCES TO BE REMOVED", type=int)
parser.add_argument("-o", help="ENTER OUTPUT FILE NAME WITH EXTENSION")
args = parser.parse_args()

fasta_path = Path(args.i)
cut_off_length = args.l

# generating out file path using the fasta path
out_filepath = fasta_path.parent/args.o

# parsing all the fasta sequences as seq records in the variable 'fasta_records'
fasta_records = SeqIO.parse(fasta_path,"fasta")

# an empty list to store the names of all the removed sequences
removed_seq = []

with open(out_filepath, "w") as fw:
    # looping over each fasta record stored inside 'fasta_records'
    for record in fasta_records:
        print(len(record.seq))
        # checking for length of each fasta sequence
        if len(record.seq) >= cut_off_length:
            # writing the required fasta sequences to output file
            SeqIO.write(record, fw, format="fasta")
            fw.write("\n")
        else:
            removed_seq.append(record.description)

print("The following sequences have been removed: ")
for seq_name in removed_seq:
    print(seq_name)

print(f"Output file successfully created at {out_filepath}")

## please contact us if you face any issues while using the code
## your personal queries are also invited










