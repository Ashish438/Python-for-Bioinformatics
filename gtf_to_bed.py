# Converting GTF format to BED format (One bed record per whole gene) using BCBIO module
# Type "python gtf_to_bed.py -i Path/of/your/GTF/file - o Output file name with extension" for running the code
# Example: python gtf_to_bed.py -i C:\Users\dell\Bos_taurus_Chr1_GTF.gtf  -o Bos_taurus_Chr1.bed
# Type "python gtf_to_bed.py -h" for help/usage description
# Output: BED file with chr, start and end of the genes present in the gtf file
# Sample input file: Bos_taurus_Chr1.gtf
# Sample output file: Bos_taurus_Chr1.bed

from BCBio import GFF
from pathlib import Path
import argparse

parser = argparse.ArgumentParser(description="Converting GTF format to BED format (One bed record per whole gene)",
                                usage= "python gtf_to_bed.py -i Path/of/your/GTF/file - o Output file name with extension")

parser.add_argument("-i", help="ENTER FULL PATH OF THE GTF FILE")
parser.add_argument("-o", help="ENTER OUTPUT FILE NAME WITH EXTENSION")
args = parser.parse_args()

GTF_path = Path(args.i)
out_filename = args.o

# generating the path of the output bed file using GTF_path
BED_path = GTF_path.parent/out_filename

# parsing records from the GTF file as a list of seq record objects
records = GFF.parse(GTF_path)

fw = open(BED_path,"w")

# looping over each record in our GTF file
for record in records:
    if type(record) is list:
        continue
    else:
        chr = record.id
        # looping over each feature within a record
        for feature in record.features:
            start = str(feature.location.start)
            end = str(feature.location.end)
            # generating the line to be written in the output bed file
            line = chr + "\t" + start + "\t" + end + "\n"
            fw.write(line)
fw.close()
print(f"Output BED file successfully generated at {BED_path}")

## please contact us if you face any issues while using the code
## your personal queries are also invited









