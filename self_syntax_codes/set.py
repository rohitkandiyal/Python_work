s = set([1,5,10,15])
f = set([5,5,10,19,31,90])

print type(s)
print s
print s.union(f)

#the practice question could also have been done in this way....
a=s.intersection(f)
print type(a)
a=list(a)
print type(a)
print a
