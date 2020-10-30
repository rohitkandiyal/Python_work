import re

#Replacing matched strings... Replacing Superman with Spiderman.

regex_obj= re.compile(r'Batman|superman',re.I)

print regex_obj.findall('I like Batman and Superman. But I think Batman has less powers than Superman.')
regex_obj= re.compile(r'superman',re.I)
print regex_obj.sub('Spiderman','I like Batman and Superman. But I think Batman has less powers than Superman.')

#matched text itself as part of the substitution

print "\nmatched text itself as part of the substitution:\n"
agentNamesRegex = re.compile(r'Agent (\w)\w*')
print agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')