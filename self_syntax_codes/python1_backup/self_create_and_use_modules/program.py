import div

x=float(raw_input("Enter the dividend:"))
y=float(raw_input("Enter the divisor:"))

a, b = div.divide(x,y)

print "The quotient is {} and the remainder is {}".format(a,b)