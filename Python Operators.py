"""
Arithmetic operators(+,-,*,/,//,**,%)
Assignment operators('='assigning is from right to left)
Comparison operators(>,<,<=,>=,==,!=)
Logical operators(and,or,not)
Identity operators(is,is not)
Membership operators(in, not in)
Bitwise operators(&,|,^)

x=2
y=3
z=4
if (not(x>y and x>z)):
    print('false')

# Arithmatic operators
# + - * / % ** //(Integer Division / Floor division)
# print(3+2)
# print(3-2)
# print(3*2)
# print(16/4)
# print(3**2)
# print(46//4)
# print(46%4)
# print(2**3)


# Assignment operator
# =
# shorthand operator: += -= *= /= %= **= //=

# x = 3
# x=x+5
# print(x)
# x+=5
# print(x)
# x-=5
# print(x)
# x*=5
# print(x)
# x/=5
# print(x)
# x**=5
# print(x)
# x//=5
# print(x)
# x%=5
# print(x)

# comparision operator
#  ==, <=,>=,!=,<,>
# print(2==3)
# print(3<=5)



# Logical operators
# and or not
# x = 5
# and
# print(x>6 and x<10)

# or
# print(x<6 or x>10)

# not
# print(not(x>6 or x>10))


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
# & | ^
# 2 10
# 3 11
#   10
# print(2 & 3)

# AND
# A B O/p
# 0 0 0
# 0 1 0
# 1 0 0
# 1 1 1

# Bitwise OR
# print(2|3)
# 2 10
# 3 11
#   11

# OR
# A B o/p
# 0 0 0
# 0 1 1
# 1 0 1
# 1 1 1

# XOR
# print(2^3)
# 2 10
# 3 11
#   01

# XOR
# 0 0 0
# 0 1 1
# 1 0 1
# 1 1 0

# left shift (<<)
# 5 -> 0000 0101
#    0 0101000
# 5*2*2*2*2
# print(5<<2)

# Right shift(>>)
# 5 0000 0101
# 000000 01
# 5//2//2
# print(5>>2)