import random

a=random.randrange(1,10)
b=(raw_input("Do you want to play the game..? (Y/N)"))
count = 0
success=0
while ((b!="n")and(b!="N")) and ((b=="Y")or(b=="y")):
	c= int(raw_input("Enter the number between 1-10:"))
	count=count+1
	
	if(a==c):
		print "You guessed it right..."
		print ("The number was {0} and you chose {1}").format(a,c)
		print ("YOU WON...!!!\n")
		success=1
		break
	else:
		if (c>a):
			print "The guess was wrong... It was higher than the number..."
		else:
			print "The guess was wrong... It was lower than the number..."

		b= raw_input("Do you want to guess again?(Y/N):")	
				

if b not in ["n","N","Y","y"]:
	print "Invalid input..."
else:	
	if (success==1):
		print "You have guessed the number in {0} attempts".format(count)
	else:
		print "Go home quitter..."
	

