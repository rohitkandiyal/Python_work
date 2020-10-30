from sys import argv

script, filename1, filename2 = argv

print filename1,filename2
'''
src_file=open(filename1)
data=src_file.read()

print data

print "The input file is %d bytes long" % len(data)
print "Copying data now..."

dest_file=open(filename2,'w+')
dest_file.write(data)
data1=dest_file.read()
print data1

print "The output file is %d bytes long" % len(data1)

src_file.close()
dest_file.close()
'''
#Copying via shutil--- From Text Manp book

import shutil

shutil.copyfile(filename1, filename2)





