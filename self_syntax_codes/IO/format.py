sub1 = "rohit"
sub2 = "26"

b = "i am  {0} and my age is {1}\n".format(sub1,sub2)
c = "The age of {} is {}".format(sub1,sub2)
print b,c
print'{0:#^11}'.format('hello')


#another way
name ="rohit"
age=26
 
print "My name is %s and age is %d" %(name,age)

print "My name is %10s and age is %4d" %(name,age)

print "My name is %0.2s and age is %4d" %(name,age)


print "+++++++++++++++++++++++++++++++++++++++++++"

#Special formatting

name=["Rohit","Jai","Rahul","Saundarya","Abhijeet","Kulkarniji","mesopotamia"]

for names in name:
	count=1
	print "%s:%d" %(names,count)
	count+=1
	
print "+++++++++++++++++++++++++++++++++++++++++++"

#So the format of above o/p is not good... we can make it better if we get the length of widest name
l=max([len(x) for x in name])
for names in name:
	count=1
	print "%*s:%d" %(-l,names,count)
	count+=1
	
print "+++++++++++++++++++++++++++++++++++++++++++"

for names in name:
	count=1
	print "%*s:%d" %(l,names,count)
	count+=1