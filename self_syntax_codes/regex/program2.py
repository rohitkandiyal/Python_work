import re


#1)- Greedy and non greedy modifiers.

print "Greedy and non greedy modifiers.\n"

'''
Python regular expressions are greedy by default, which means that in ambiguous
situations they will match the longest string possible. The non-greedy version is the one 
which matches the shortest string possible.

(Ha){3,5} can match three, four, or five instances of Ha

Note that the question mark can have two meanings in regular expressions: declaring a
nongreedy match or flagging an optional group. These meanings are entirely unrelated.
'''

regex_obj= re.compile(r'(Ha){3,5}')
mo = regex_obj.search('HaHaHaHaHa')
print mo.group()

regex_obj= re.compile(r'(Ha){3,5}?')
mo = regex_obj.search('HaHaHaHaHa')
print mo.group()

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#2)-findall() Method

print "\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"
print "findall() method\n"
regex_obj= re.compile(r'(Batman|Superman)')

print regex_obj.findall('I like Batman and Superman. But I think Batman has less powers than Superman.')
print "\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"
print "Difference between pipe and []... Above one is pipe usage. \n"
regex_obj= re.compile(r'[Batman,Superman]')
print regex_obj.findall('I like Batman and Superman. But I think Batman has less powers than Superman.')

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#3)-Negating a search. I think negate works only within []

print "\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"
print "Negating a search\n"

vowelRegex = re.compile(r'[aeiouAEIOU]')
print vowelRegex.findall('Robocop eats baby food. BABY FOOD.')

vowelRegex = re.compile(r'[^aeiouAEIOU]')
print vowelRegex.findall('Robocop eats baby food. BABY FOOD.')

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#4)-Wildcard character(.) -- Matches anything other than a newline(\n) 

#(.) is like ? in Unix. 
#(.*) is like * in Unix.  

print "\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"
print "Wildcard character\n"


atRegex = re.compile(r'.at')
print atRegex.findall('The cat in the hat sat on the flat mat.')		#flat will not be matched.

atRegex = re.compile(r'.*at')
print atRegex.findall('The cat in the hat sat on the flat mat.')

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#5)-Case insensitive search

print "\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"
print "Case insensitive search\n"

regex_obj= re.compile(r'(batman|superman)',re.IGNORECASE)		#or re.I

print regex_obj.findall('I like Batman and SUPERMAN. But I think baTman has less powers than sUperMan.')