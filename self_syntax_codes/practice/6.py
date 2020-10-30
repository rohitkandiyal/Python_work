import copy

str = raw_input("Enter a string: ")

str = list(str)
#
#Using the concept of deep/shallow copy
#

str1=copy.deepcopy(str)

str1.reverse()

if(str==str1):
	print "Yes"
else:
	print "No"
