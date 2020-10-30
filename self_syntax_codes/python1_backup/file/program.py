from sys import argv

'''script, filename = argv

txtr = open(filename)
txtw = open(filename,'w')			#as soon as we open a file in write mode then all the existing content in the file gets deleted...
									#If you open the file with 'w' mode, then do you really need the target.truncate()? NO.... So we use a for appending

txtw.write("This is the 1st content I am writing in this file...")
print "Here's your file:--> %r" % filename
print txtr.read()


print "Deleting the content of the file"
txtw.truncate()
print txtr.read() 

print "Writing again"
txtw.write("This is the 2nd content I am writing in this file...")

print "The file now has:\n"
print txtr.read()'''

#######################################################################################


#How to open the file in one than more modes...
#txt = open(filename1,'w+')






