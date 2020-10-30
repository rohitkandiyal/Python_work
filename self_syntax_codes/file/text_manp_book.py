

#	PYTHON

from sys import argv

script, filename = argv
txt = open(filename)
#Below will print the individual lines...

for line in txt.readline():
	print line
txt.seek(0)
print '''\n++++++++++++++++++++++++++\n'''

for line in txt.readlines():
	print line

txt.seek(0)
print '''\n++++++++++++++++++++++++++\n'''

for line in txt.readlines():
	if "Rohit" in line:
		print line
txt.seek(0)
print '''\n++++++++++++++++++++++++++\n'''


for line in txt.readlines():
	if line.startswith("Rohit"):
		print line
		print line.upper()
		a=list(line)
		a.reverse()
		print ''.join(a)

txt.seek(0)
print '''\n++++++++++++++++++++++++++\n'''

#Adding something at the start of every line:
c=0
for line in txt.readlines():
	c=c+1
	print "Line {}: {}".format(c,line)