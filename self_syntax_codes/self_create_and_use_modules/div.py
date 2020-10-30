# file : div.py
def divide(a,b):
	q = a//b # If a and b are integers, q is an integer
	r = a - q*b
	return (q,r)