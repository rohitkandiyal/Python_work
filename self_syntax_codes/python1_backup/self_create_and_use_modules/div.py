# file : div.py
def divide(a,b):
	q = a//b # If a and b are integers, q is an integer
	r = a - q*b
	return (q,r)

if  __name__ == 'main' or __name__ == '__main__' :
	print " the div has been directly compiled"
else:
	print "the div.py has been called as a module or is not directly interpreted"