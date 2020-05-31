# counting ATGC in your multiple fasta file using biopython and generating bar plots for the same using matplotlib

import numpy as np
from Bio.SeqIO import parse
from matplotlib import pyplot as plt
count={"A":[],"G":[],"C":[],"T":[]}
header=[]
for sec_rec_obj in parse("path of your fasta file","fasta"):
    count["A"].append(sec_rec_obj.seq.count("A"))
    count["G"].append(sec_rec_obj.seq.count("G"))
    count["C"].append(sec_rec_obj.seq.count("C"))
    count["T"].append(sec_rec_obj.seq.count("T"))
    header.append(sec_rec_obj.name)

#CODE FOR PLOTTING:

x_index=np.arange(len(header))   
width=0.2
fig,ax=plt.subplots()
ax.bar(x_index-width, count["A"],width=width,label="Count of A",color="yellow")
ax.bar(x_index, count["G"],width=width,label="Count of G",color="green")
ax.bar(x_index+width, count["C"],width=width,label="Count of C",color="blue")
ax.bar(x_index+(2*width), count["T"],width=width,label="Count of T",color="red")
ax.set_xticks(x_index) 
ax.set_xticklabels(header,rotation=45,ha="right")
ax.legend()
ax.set_xlabel('headers of fasta') 
ax.set_ylabel('count')
plt.show()

##please leave a message if you want a text version of this code or if you face any issues while using the code 
##your personal queries are also invited

	
