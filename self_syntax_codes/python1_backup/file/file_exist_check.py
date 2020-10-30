from os.path import exists

file=raw_input("Enter the filename which is to be checked for existence...?")

print "Does the file exist? %r" % exists(file)