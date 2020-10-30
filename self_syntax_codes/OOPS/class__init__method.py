# Now there is another thing __init__ method

"""
we above wanted to have two attributes for each object of class ftp_team... so we did below :

class ftp_team:
	name="definition"
	experience=0
	
if we do below then there is an error:

class ftp_team:
	str name
	int experience	
	
as this is not allowed in python..... So here comes the role of __init__ method.... 

__init__ method is primarily used to pass some attributes to the object as soon as the object/instance is created....

let's rewrite the code in class.py program using __init__ method.....

"""

class ftp_team:
	"This is the documentation of this class..."
	def __init__(self,name,experience):
		self.name=name
		self.experience=experience
	
	def print_details(self):
		print "The employee name is {} and the years of experience is {}".format(self.name,self.experience)
		
		
##Simple usage....

emp1=ftp_team("ROHIT",5)
emp1.print_details()
print emp1.__doc__
print ftp_team.__doc__

#using some inbuilt functions to get details
print callable(emp1)
print dir(emp1)
print type(emp1)
print isinstance( emp1, ftp_team )
print issubclass( ftp_team, object ) 
print repr(emp1)
print vars(emp1)


"""		complex usage is below.... this is commented to not to be confused....

x=raw_input("Please enter the number of employees for which the data is to be entered:")
x=int(x)

while(x>0):

	name = raw_input("Please enter employee's name:")
	experience = raw_input("Please enter employee's experience(years):")
	
	emp=ftp_team(name,experience)
	emp.print_details()
	x=x-1
"""

