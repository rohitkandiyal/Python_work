a = ["r", "o", "h", "i", "t", "k", "a", "n", "d", "i", "y", "a", "l"]

a.insert(5, "\n")
print(a)
print("".join(a))

print("############################################")

a.pop(5)
print(a)

print("############################################")
a.remove("a")
print(a)

# how many i's in my name
print(a.count("i"))
print(a.count("z"))


# to remove all i's in my name
while "i" in a:
    a.remove("i")

print(a)
