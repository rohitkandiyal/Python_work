def foo(x,y):
	"This is a function to add two numbers..."
	return x+y
	
print(foo.__doc__)
print(foo.__name__)


print foo(3,8)

print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"

#lambda function

mul=lambda x,y: x * y

print foo(3,8)
print mul(3,8)

print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"

#Use of map()
#Suppose I want a function to be applied to the members of a list or lines of a file

sqr=lambda a: a * a
b=[1,3,5,2,8,7,9,4,6,17]

print map(sqr,b)
print map(sqr,map(sqr,b))

#now let's make the above example more FP compliant

a=map(lambda x:x*x , b)
print(list(a))

print(map(lambda x:x*x , b))		#So we don't hv the need to define sqr function here.


print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"

#Use of filter()
#Find odd numbers in a list

print filter(lambda x:(x%2)==0 , b)

print "\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"

#Use of reduce()
#Find largest number in a list

print reduce(lambda a,c: a if (a > c) else c , b)

print "\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"





	















