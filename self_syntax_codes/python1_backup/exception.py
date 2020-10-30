try:
	f = open("foo")
	print "Hi man..."
except IOError, e:
	print "Unable to open foo:", e
	print "Hi"

print "Hi There..."