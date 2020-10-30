from sys import argv

script, filename = argv
txt = open(filename)

a= txt.readline()
print a.split(' ')
print a.split(':')

print sorted(a)

#see chapter 25 of LPTHW