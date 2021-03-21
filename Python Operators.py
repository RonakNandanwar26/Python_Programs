"""
Arithmetic operators
Assignment operators
Comparison operators
Logical operators
Identity operators
Membership operators
Bitwise operators
"""

# Arithmatic operators
# + - * / % ** //
# print(3+2)
# print(3-2)
# print(3*2)
# print(46/4)
# print(3**2)
# print(46//4)


# Assignment operator
# = += -= *= /= %= **= //=

# x= 3
# x = x+5
# print(x)
# x+=5


# comparision operator
# ==, <=,>=,!=,<,>
# print(2!=3)


# print(3!=5)


# Logical operators
# and or not
x =5
print(not(x>4 and x<10))

# Identity Operators

# x=5
# y=x
# z=4
#
# print(x is y)
# print(id(x))
# print(id(y))
# print(x is not z)
# print(id(z))

# Membership Operators
# in, not in
# x = [1,2,3,45]
# print(8 not in x)

#  Bitwise Operators
# 2 10
# 3 11
#   10
print(2 & 3)

# AND
# 0 0 0
# 0 1 0
# 1 0 0
# 1 1 1

# Bitwise OR
print(2|3)
# 10
# 11
# 11



# OR
# 0 0 0
# 0 1 1
# 1 0 1
# 1 1 1

print(2^3)
# 10
# 11
# 01

#
# XOR
# 0 0 0
# 0 1 1
# 1 0 1
# 1 1 0

# left shift
# 5  00 010100
# 0001 0100

# print(5<<2)

# Right shift
# 5 000000 01
# 000000 01
# print(5>>2)