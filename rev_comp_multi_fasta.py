# Finding reverse complement of all the sequences in a multi fasta using biopython

# Type: "python rev_comp_multi_fasta.py -i Path of your multi fasta file -o Output file name with extension" for running the code
# Example: python rev_comp_multi_fasta.py -i C:\Users\dell\Desktop\test\sample_multi_fasta.fasta -o rev_comp_multi_fasta.fasta

# Type: "python rev_comp_multi_fasta.py -h" for help/usage description

# Output: A fasta file having reverse complement of all the sequences

# Sample input file: sample_multi_fasta.fasta
# Sample output file: rev_comp_multi_fasta.fasta

import argparse
from Bio import SeqIO
from pathlib import Path

parser=argparse.ArgumentParser(description="Finding reverse complement of all the sequences in a multi fasta, USAGE: python rev_comp_multi_fasta.py -i Path/to/multi/fasta/file -o Output.fasta")
parser.add_argument("-i", help="ENTER FULL PATH OF THE MULTI FASTA FILE")
parser.add_argument("-o", help="OUTPUT FILE NAME WITH EXTENSION")
args = parser.parse_args()

input_path = Path(args.i)
out_path = input_path.parent/args.o

fasta_records = SeqIO.parse(input_path,"fasta")
new_records = []

for fasta_record in fasta_records:
	fasta_record.description = fasta_record.description + "(reverse_complement)"
	fasta_record.seq = fasta_record.seq.reverse_complement()
	new_records.append(fasta_record)

with open(out_path,"w") as fw:	
	SeqIO.write(new_records,fw,"fasta")

print("Output file successfully generated at: ",out_path)

## please leave a message if you face any issues while using the code 
## your personal queries are also invited

