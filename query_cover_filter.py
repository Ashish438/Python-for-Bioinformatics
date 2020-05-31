
# finding query coverage with filter from the output file of offline blast and writing the output of this code to a different file

input_path="path of your blast output file"

input_path_list=input_path.split("/")
input_filename=input_path_list[-1]

choice = input("Please enter your choice as 1 or 2: ")
if choice == 1:
    out_file_path=input_path.strip(i_filename)+"eq_100"+"output_"+input_filename

elif choice == 2:
    out_file_path = input_path.strip(i_filename) + "less_than_100_"+"output_" + input_filename

else:
    out_file_path = input_path.strip(i_filename) + "output_" + input_filename

o_file=open(out_file_path,"w")

for line in i_file:
    col=line.split("\t")
    x=int(col[3])-int(col[4])-int(col[5])
    y=int(col[12])
    qc=(x/y)*100
    qc_line = (line.strip("\n")) + "\t" + str(qc) + "\n"
    if choice == 1:
        if qc == 100:
            o_file.write(qc_line)
    elif choice ==2:
        if qc < 100:
            o_file.write(qc_line)
    else :
        o_file.write(qc_line)

i_file.close()
o_file.close()
   
##please leave a message if you want a text version of this code or if you face any issues while using the code 
##your personal queries are also invited

	
