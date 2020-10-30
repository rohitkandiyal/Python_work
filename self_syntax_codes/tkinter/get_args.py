or_home=r"C:\MdbBOT\Oracle"+"\\"

file=or_home+"config\\patch\\Patching.txt"
#print file
txt = open(file)
args=[]
for line in txt.readlines():
	args.append(line.split(",")[1])
	#print type(line)

#print args
arg=[]
for a in args:
	#print type(a)
	a=a.replace("\n","")
	arg.append(a)

print arg[0]