def sum_of_digits(num):
	sum=0
	while num:
		sum=sum+(num%10)
		num //= 10
	return sum



N = int( raw_input("Please enter the number: ") )
a=len(str(N))
'''if (N<10):
	for i in range((2*N),11*N,N):
		if ((sum_of_digits(i)) ==N):
			print i
			break'''
			
if (0<N<=100):
	
	for i in xrange((2*N),999999999,N):
			if ((sum_of_digits(i)) ==N):
				print i
				break
		



	