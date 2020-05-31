# finding query coverage from the output file of offline blast and writing the output of this code to a different file

input_file="path of your blast output file"

l1=input_file.split("/")
file_name=l1[len(l1)-1]

out_path=input_file.strip(file_name)
out_file_path=out_path+"output_"+file_name

fr=open(input_file,"r")

fw=open(out_file_path,"w")

for line in fr:
	col=line.split("\t")
	EML=int(col[3])-int(col[4])-int(col[5])
	QL=int(col[12])
	QC=(EML/QL)*100
	#print(QC)
	line=line.strip("\n")
	nl=line+"\t"+str(QC)+"\n"
	#print(nl)
	fw.write(nl)

##please leave a message if you want a text version of this code or if you face any issues while using the code 
##your personal queries are also invited

	
