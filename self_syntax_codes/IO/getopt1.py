#!/bin/python

import sys,getopt

#print "Arguments are : {}".format(sys.argv[1:])
#print "Number of args are: {}".format(len(sys.argv[1:]))

valid_args={
			"-o":"This is a single char option with no args-- Mention the o/p file",
			"-v":"This is a single char option with args-- for verbose o/p",
			"-h":"Display this message",
			"--output":"This is a single char option with no args-- Mention the o/p file",
			"--verbose":"This is a long option with no args-- for verbose o/p",
			"--version":"This is a long option with args-- To display the version",
			"--help":"Display this message"
		}


l1= max([len(x) for x in valid_args.keys()])
l2=max([len(x) for x in valid_args.values()])

def usage():
	print "\n\nBelow are the valid options:\n"
	for key in valid_args: 
		print "%*s : %*s" %(-l1,key,-l2,valid_args.get(key))

def parse_opts():
	version = '1.0'
	verbose = False
	output_filename = 'default.out'
	
	try:
		options, remainder = getopt.getopt(sys.argv[1:], 'o:vh', ['output=','help','verbose','version=',])
	except getopt.GetoptError :
		print "\nInvalid Options : "+' , '.join(sys.argv[1:])
		usage()
		return None
	
	print 'OPTIONS   :', options
	print 'REMAINDER   :', remainder
	
	for opt, arg in options:
		if opt in ('-o', '--output'):
			output_filename = arg
		elif opt in ('-v', '--verbose'):
			verbose = True
		elif opt == '--version':
			version = arg
		elif opt in ('-h','--help'):
			usage()
		
	print 'VERSION   :', version
	print 'VERBOSE   :', verbose
	print 'OUTPUT    :', output_filename
	print 'REMAINING :', remainder	
		
		
	
def parm_test():
	if len(sys.argv[1:])<1:
		print "\n Error: Please provide the required options..."
		usage()
	else:
		parse_opts()
			
if  __name__ == 'main' or __name__ == '__main__' :
	parm_test()	
else :
	usage()
		
	



