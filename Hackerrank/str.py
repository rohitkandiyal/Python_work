a = "roHIt"

print(a.swapcase())
print(a.capitalize())
print(a.casefold())
# print(a.count())
print("############################################")

a = 1.2233

print(type(a))
print(format(a, ".2f"))

print("############################################")
a = "ROHIT KANDIYAL IS MY NAME"
print(a.split())
print(a.title())

print("############################################")
a = "ROHIT"

print(a.ljust(10, "&"))
print(a.rjust(10, "&"))


print("############################################")
a = "++++rohi+tkkk++++++++"
print(a.strip("+"))
print(a.rstrip("+"))
print(a.lstrip("+"))

print("############################################")
a = "AADAkjakAADADADAJHKL"

print(a.count("AD"))

#but issue with ADA as response shud be 3
print(a.count("ADA"))

count = 0
while "ADA" in a:
    i = a.find("ADA")
    count = count + 1
    a = a[i+1:]

print(count)

print("############################################")
a = "P"
print(chr(ord(a) + 1))



