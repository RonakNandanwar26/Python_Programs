# if_else statement

# Python supports the usual logical conditions from mathematics:
#
# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b

# An "if statement" is written by using the if keyword.

# syntax
# if condition:
# 	o/p code

# a = 33
# b = 200
# if a < b:
#     print("a is greater than b")

# a = 33
# b = 200
# if b > a:
#     print("b is greater than a")

# if_else
# a = 200
# b = 33
# if b > a:
#     print("b is greater than a")
# else:
#     print("a is greater than b")


# Elif

a = 36
if a<10:
    print("a is greater than 10")
elif a<20:
    print("a is greater than 20")
elif a<30:
    print("a is greater than 20")
else:
    print('a is higher value')


# shorthand if
a=10
b=20
if a <= b: print("a is greater than b")

# shorthand if_else
print('A') if a<b else print('B')

# above technique of writing if_else is also known as ternary operator or
# conditional expression

# One line if else statement, with 3 conditions:
a = 330
b = 330
print("A") if a > b else print("equal to =") if a == b else print("B")

# Logical operators

# AND
a = 200
b = 33
c = 500
if (a > b and c > a):
    print("Both conditions are True")

# or
a = 200
b = 33
c = 500
if b > a or a > c:
    print("At least one of the conditions is True")
else:
    print('None of the condition is true')


#  Nested if

x = 15
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")




# pass statement
#
# a = 33
# b = 200
#
# if b > a:
#     pass