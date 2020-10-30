a=[1,2,3,-3,-5,0,4,67,90]


print "###Below is the output of loop with continue####"

for x in a:
	if(x<0):
		continue
	else:
		print(x)
		
print "\n\n###Below is the output of loop with break####"

for y in a:
	if(y==0):
		break
	else:
		print(y)

