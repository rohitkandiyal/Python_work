a=[1,2,3,4,5,6,7,8,9,10,11,12]

print type(a)
print len(a)
print a[-1]

#Slicing
print a[2:6]
print a[:6]
print a[6:]

#Slicing with stride
print a[:6:2]				#produced subsequence is the elements s[i], s[i+stride], s[i+2*stride]
