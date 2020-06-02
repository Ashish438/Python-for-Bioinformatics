
# GO (Gene Ontology) enrichment analysis using python

import pandas as pd
import xlsxwriter
import os

in_path = "enter path of your input excel file"
# e.g: in_path = "C:\Users\dell\Desktop\testing_go_en\GO_enrichment_input.xlsx"

sheet_name = "enter sheet name"
# e.g: sheet_name = "UpRegulated"

sheet_col_name_list = [enter the names of the three GO columns]
# e.g: sheet_col_name_list = ["GO Biological Process Term","GO Cellular Component Term","GO Molecular Function Term"]

def Go_En(in_path,sheet_name,sheet_col_name_list):
    #reading our input excel file and specifying the sheet name and converting it to dataframe:
    
    df=pd.read_excel(in_path,sheet_name)

    in_path=in_path.strip("GO_enrichment_input.xlsx")
    out_path=in_path+sheet_name  #sheet_name is same as our folder name and out_path is where the folder is created
    try:
        os.mkdir(out_path)
    except:
        print("it will overwrite")
    workbook_path=out_path+"/"+sheet_name+"_"+"GO_Enrichment_Analysis.xlsx"
    workbook = xlsxwriter.Workbook(workbook_path)

    for sheet_col_name in sheet_col_name_list:
        #exracting the GO term we want to work on from the dataframe
        working_col=df[sheet_col_name]  #working_col is a series
        working_col.dropna(inplace=True)  #removing NAN values from our series

        gene_sym_GO = df[["Gene Symbol", sheet_col_name]]
        gene_sym_GO = gene_sym_GO.dropna()
        #print(gene_sym_GO)
        #for each string present in each row of our series
        #we replace the ",GO" with # and split the strings with "#"
        working_col=working_col.str.replace(",GO","#").str.split("#")

        #now each row of our series has a list instead of a string

        list1=[]
        for row in working_col:    #looping over each row i.e a list, in our series

            for item in row:   #looping over each term in our list
                # splitting each string of a list of a row by "~"
                #this will again create a list
                #extract the string at the index 1 of our generated list and remove "," from its end
                item=item.split("~")[1].strip(",")

                #appending the extracted string to a list
                list1.append(item)
        #print(list1)


        #assigning our list to a set to remove duplicates
        s1=set(list1)
        #print(len(s1))
        #print(len(list1))

        list2=[]
        for te in s1:
            x=()
            #x is a tuple
            x=(te,list1.count(te))

            list2.append(x)


        df1=pd.DataFrame(list2)




       #FINDING CORRESPONDNG GENE SYMBOL FOR RESPECTIVE GENE ONTOLOGY TERM
        #taking all the GO terms in 0th column of df1 in the variable term
        #df1[0] returns a series which is stored in term
        term = df1[0]
        #print(term)
        gene_symbol = [] #empty list to contain all the gene symbols for respective GO in the term series

        #looping over each GO term in term
        for item1 in term:
            counter=0  #counter variable
            gene_sym_str="" #stores the gene symbol for each GO term

            #looping over each row in our dataframe gene_sym_GO
            #it contains the columns of Gene Symbol and Gene Ontology(input)

            i=0  # i will store the no.of rows in gene_sym_GO
            for index, row in gene_sym_GO.iterrows():

                i+=1 #incrementing i for each run of loop


                #converting our series 'row' to list which has gene symbol at 0th index
                #and Gene Ontology Term(input) at 1st index
                #i.e row_list[0]=gene symbol and row_list[1]=gene ontology term(input)
                row_list = row.tolist()


                #comparing each GO term(output) to GO term(input) for each row
                if item1 in row_list[1]:

                    counter+=1
                    if counter > 1:  #will execute if item1 matches to more than one rows
                        gene_sym_str += ","+row_list[0]


                    else: #will execute ony if item1 matches to only one row
                        gene_sym_str=row_list[0]

            if i==gene_sym_GO.shape[0]:  #will execute only on the last iteration of the gene_sym_GO for loop
                # appending the final result in gene_symbol after
                gene_symbol.append(gene_sym_str)


        #print(gene_symbol)
        #print(len(gene_symbol))



        #Adding gene_symbol to df1 by converting it to a dataframe
        #   ERROR WAS IN INSERTING gene_symbol list INTO DATAFRAME


        gene_symbol_df=pd.DataFrame(gene_symbol)
        #print(gene_symbol_df)
        #print(df1[0])
        concat_df=pd.concat([gene_symbol_df, df1],axis=1)
        concat_df.columns=[0,1,2]
        concat_df.sort_values(by=2,inplace=True,ascending=False)
        #print(concat_df[[0,1]])



# Writing Data To Xlsx worksheets : Gene Symbol, GO term, Count

        worksheet = workbook.add_worksheet(sheet_col_name)
        bold = workbook.add_format({'bold': 1})

        headings = ['Gene Symbol','Term', 'Count']

        worksheet.write_row('A1', headings, bold)
        worksheet.write_column('A2', concat_df[0])
        worksheet.write_column('B2', concat_df[1])
        worksheet.write_column('C2', concat_df[2])

        #creating a chart object
        chart1=workbook.add_chart({'type': 'pie'})
        chart1.add_series({
                          'categories': [sheet_col_name,1,1,20,1],
                          'values': [sheet_col_name,1,2,20,2],
                          'data_labels':{'value':True},
        })

        # Add a title.
        chart1.set_title({'name': sheet_col_name})

        # Set an Excel chart style. Colors with white outline and shadow.
        chart1.set_style(10)


        # Insert the chart into the worksheet (with an offset).
        worksheet.insert_chart('E2', chart1, {'x_scale': 2.5, 'y_scale':2.5})


    workbook.close()
    return workbook_path

output_path = Go_En(in_path,sheet_name,sheet_col_name_list)

print("file successfully generated at: ",output_path)

##please leave a message if you want a text version of this code or if you face any issues while using the code 
##your personal queries are also invited

	
