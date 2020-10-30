#This program stores a randomly generated sensor states S1-S4
#The outside and inside temperatures too are evaluated randomly
#Written on 04/23/2018

import sys
import os
import time
import random

PATH=r"C:\Users\kandiyal\Desktop\for work\python\project" 		#Change as per the machine
try:
	os.chdir(PATH)
except,e:
	PATH=os.getcwd()

t=time.asctime(time.localtime())
t=t[4:19]

txtw = open("data.txt",'a')
s=random.randint(1,4)

states=	{
			"1":"Doors Closed;Person not present",
			"2":"Doors Opened;Person not present",
			"3":"Doors Opened;Person present",
			"4":"Doors Closed;Person present"
		}
		
o_temp=random.randint(-15,25) 
i_temp=random.randint(10,30)	
occ=0				
if(s==3 or s==4):
	occ=1
txtw.write(t+" : State "+str(s)+" - ("+states[str(s)]+")\t\t"+occ+"\t"+o_temp+"\t"+i_temp+"\n")
