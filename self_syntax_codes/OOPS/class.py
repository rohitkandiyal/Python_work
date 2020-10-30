class ftp:			#This is a classic class as there is no inheritance from object
	name="abc"
	emp_experience=0
	
#now we will define an instance/object of this class....

rohit=ftp()
rohit.name="Rohit Kandiyal"
rohit.emp_experience=5

print "The employee name is {} and the years of experience is {}".format(rohit.name,rohit.emp_experience)


#
#now what we can do is define a function in class only which will ask for the parameters from users for different objects of the class....
#
#similarly there will be a function to print the received values....



#<<<<<<PROGRAM 2>>>>>>

class ftp_team(object):
	name="definition"
	experience=0
	
	def ask_from_user(self):
		self.name = raw_input("Please enter employee's name:")
		self.experience = raw_input("Please enter employee's experience(years):")
	
	def print_details(self):
		print "The employee name is {} and the years of experience is {}".format(self.name,self.experience)
		
		

emp1=ftp_team()
emp2=ftp_team()

emp1.ask_from_user()
emp2.ask_from_user()

emp1.print_details()
emp2.print_details()




		
	
	





