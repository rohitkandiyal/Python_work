#code for learning if-- skillportal



i,x,y=2,10,100

if(x<y):
	print "x is less than y"
	x=x*i		
	i=i+1											
else:	
	print "x is not less than y"

if 5<10:
	print "the evaluation is true"

#Types of if statements

#Alphabetic ordering
print 'cat' < 'dog'	

#Uppercase before lowercase
print 'Cat' < 'cat'

#All uppercase before lowercase
print 'Dog' < 'cat'


num=10

if 0<num<12:
	print "Yes"

#O is FALSE
if (1-1):
	print "1st yes"
else:
	print "2nd yes"
	
#Boolean evaluations

if (1-1) and (2+2):
	print "False and true"
else:
	print "this is else."

if (1-1) or (2+2):
	print "False OR true"
else:
	print "this is 2nd else."
	
	
#Basic boolean maths laws follows here too....

print type(True)