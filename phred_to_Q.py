
# function Qtophred to convert Q value to phred score
# function phredtoQ to convert phred score to Q value  

def Qtophred(Q):
	return chr(Q+33)

print(Qtophred(10))


def phredtoQ(phred):
	return (ord(phred)-33)

print(phredtoQ("+"))

##please leave a message if you want a text version of this code or if you face any issues while using the code 
##your personal queries are also invited

	
