from sys import argv

script, filename = argv
txt = open(filename)
#Below will print the individual lines...
'''print txt.readline()		#1st line...
print txt.readline()		#2nd line....
print txt.readline(9)		#prints first 9 chars of 3rd line....

txt.seek(0)					#rewind back the file	
print txt.readline()		#again prints 1st line as seek has set the counter to 0

txt.seek(0)	
'''
for line in txt.readlines():
	print type(line)
	print line.replace("\n","<br>")
	
	
print type(txt.readlines())

print ""
txt.seek(0)
print len(txt.readlines())
	


	



