import re
from sys import argv

script, filename = argv
txtr = open(filename)
#print txtr.read()

regex_obj= re.compile(r'Batman|superman',re.MULTILINE|re.I)
print regex_obj.findall(txtr.read())
txtr.seek(0)
regex_obj= re.compile(r'''(
[a-zA-Z0-9._%+-]+ 					# username
@ 									# @ symbol
[a-zA-Z0-9.-]+ 						# domain name
(\.[a-zA-Z]{2,4}) 					# dot-something
)''', re.VERBOSE|re.MULTILINE)

print regex_obj.findall(txtr.read())