a = int(raw_input("Enter a number:"))
b = [1]

for i in range(2,((a/2)+1)):
	if (a%i == 0):
		b.append(i)
		
print "The factors of {0} : {1} \n".format(a,b)