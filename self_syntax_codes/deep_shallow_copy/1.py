# Normal assignment is basically a reference to same object

num = [1, 2, 3, 4, 5, 6]

num1 = num

num1[0] = 5

print(id(num))      # prints mem location of num
print(num)
print(id(num1))     # prints mem location of num1
print(num1)

# So both num and num1 will be changed with new as both are referencing to same object as per id() o/p

####################################################################################################

# Shallow copy

import copy

num2 = [5, 6, 7, 8]
num3 = copy.copy(num2)

num3[0] = 13

print(id(num2))      # prints mem location of num
print(num2)
print(id(num3))     # prints mem location of num1
print(num3)

# so both have different mon locations and hence change in one does not change another

####################################################################################################

# Deep copy
# Now let's say we have a nested list so the elements of internal list are referenced and not copied.

num4 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
num5 = copy.copy(num4)

# different id
print(id(num4))
print(id(num5))

num5[0][1] = 1000

# same id
print(num4)
print(id(num4[0][1]))
print(num5)
print(id(num5[0][1]))


# so we have a copy of list but not of it's internal objects
# HENCE we use deepcopy
