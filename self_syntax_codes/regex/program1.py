import re

print "\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"
'''Single line string regex matching'''


regex_obj= re.compile(r'\d{3}-\d{8}')			#regex_obj is the regex object created.
mo = regex_obj.search('My number is 011-22576894')			
print mo.group()

print "\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"
'''Grouping is done via regex. In this case grouping can be done to get STD code'''

regex_obj= re.compile(r'(\d\d\d)-(\d\d\d\d\d\d\d\d)')
mo = regex_obj.search('My number is 011-22576894')
print "The contact number is: " + mo.group()
print "The STD code is: " + mo.group(1)
print mo.groups()

print "\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"

'''Piping in regex. r'Batman|Tina Fey' will match either 'Batman' or 'Tina Fey'.
Will give the first occurence. But you can find all matching occurrences with the findall() method discussed later.

[] also does the same kind of job but that is for just one character. [a-zA-Z0-9] will match all lowercase letters, uppercase letters, and
numbers.'''

regex_obj= re.compile(r'(Batman|Superman)')

mo = regex_obj.search('I like Batman and Superman. But I think Batman has less powers than Superman.')
print mo.group()
mo = regex_obj.search('I like Batman and Superman. But I think Batman has less powers than Superman.')
print mo.group()

print "\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"

'''Optional Matching. This can be used to get types of format in which there can be a number'''

regex_obj= re.compile(r'[+,\(]*(\d{2})?[-,\s,.,)]*(\d{10})')		#Note that ) in [] is not preceded by \. This is bcoz inside the square brackets, the normal regular expression symbols
																	#are not interpreted as such. This means you do not need to escape them.
																	
mo = regex_obj.search('My number is +(91))--7798982966')			# as we are using greedy modifier then only )- after 91 is matched.
print mo.group()	

print "\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"


















