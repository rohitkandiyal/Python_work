sub1 = "rohit"
sub2 = "26"

b = "i am  {0} and my age is {1}\n".format(sub1,sub2)
c = "The age of {} is {}".format(sub1,sub2)
print b,c
print'{0:#^11}'.format('hello')
#print eval(sub1)

#another way
name ="rohit"
age=26
 
print "My name is %s and age is %d" %(name,age)

print "My name is %10s and age is %4d" %(name,age)

print "My name is %0.2s and age is %4d" %(name,age)

# See below to understand the difference between %s,%d and %r
#%r is used for debugging and hence gives the output as it is.... hence called raw formatting....

print "months are: %s" % "\nJan\nFeb\nMar"

print "months are: %r" % "\nJan\nFeb\nMar"
