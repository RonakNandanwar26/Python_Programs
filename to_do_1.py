#  # format
# # as we can't combine string and numbers using + we can cobine them using .format
#
# age = 21
# txt = 'My age is {}'
# print(txt.format(age))
# #
# quantity = 3
# item_no = 567
# price = 49.95
# print('I want {2} piece of item {0} for {1} dollars'.format(quantity,item_no,price))
# #


# Boolean

# print(10>=9)
# print(9<=10)
# print(10==9)

#Arithmatic operators
# + - * ** / // %
# x = 10 
# x = x + 2
# print(x)
# x += 2
# print(x)

# print(x)
#
# x = x - 2
# print(x)
# x -= 2
# print(x)
#
# x = x * 2
# print(x)
# x *= 2
# print(x)
#
# x = x / 2
# print(x)
# x /= 2
# print(x)
#
# x = x % 2
# print(x)
# x %= 2
# print(x)
#
# x = x // 2
# print(x)
# x //= 2
# print(x)
#
# x = x ** 2
# print(x)
# # x **= 2
# print(x)
#
# x = x + 2
# print(x)
# x += 2
# print(x)
#
# x = int(x) & 2
# print(x)
# x &= 2
# print(x)
#
# x = x | 2
# print(x)
# x |= 2
# print(x)




# comparision operator

# x = 34
# y = 10
#
# print(x==y)
# print(x!=y)
# print(x>y)
# print(x<y)
# print(x>=y)
# print(x<=y)


# # logical operator
# x = 10
# y= 5
# print(x==10 and x<1)
# print(y == 10 or y<5)
# print(not(x>0 and y<11))


# Membership operator

# x = 'Ronak'
# print('on' in x)
# print('orange' not in x)

# Identity operator
# is 
# is not
# x = ['apple','banana' , 1]
# y = ['apple','banana' , 1]
# z = x
# print(x is z)
# print(x is not y)




# Bitwise operator
# &
# x = 3
# x = x & 2
# print(x)
# x &= 2
# print(x)

# |
#
# x = x | 2
# print(x)
# x |= 2
# print(x)

# ^
#
# x = x ^ 2
# print(x)
# x |= 2
# print(x)


# x = 15
# # << left shift
# pr6b  int(5 << 2)
# # right shift
# print(5 >> 2)
# # ~
# print(~x)














# New datatypes
# list
# tuple
# set
# dictionary


#  List
# # # access value by index
# list is an ordered and indexed and mutable data type
# x = ['apple', 'banana',{1:23},34, 1,-1,1.5,1+2j]
# print(type(x))
# print(x[-7])
# print(x[::2])
# print(x[-3:-1])
# print(x[-3:-1:2])
# # length of list
# print(len(x))

# print(x[1])
# add item using append
# x.append('orange')
# print(x)


# insert item at specific index in list using insert(index, 'item')
# x.insert(2,'watermelon')
# print(x)
# print(x[1])
# print(x[2])

# delete specific element of list using remove
# x.remove('orange')
# print(x)


# pop method
# x.pop()
# print(x)

# x.pop(1)
# print(x)



# del list[0]
# del x[0]
# print(x)

# del x
# print(x)


# clear
# x.clear()
# print(x)



# lst =['orange', 'banana']
# lst1 = [1,2,3]
# # join 2 list using +
# lst2 = lst1 + lst
# print(lst)
# print(lst1)
# print(lst2)



# join 2 list using extend
# lst.extend(lst1)
# print(lst)
# print(lst1)


# orange-banana
# join element of list using join method e.g '-'.join()list
# print(lst1)
# lst1 = ['1','2','3']
# lst2 = '-'.join(lst1)
# print(lst2)
# # print(type(lst2))

# 1-2-3

# x    y
# 12 <-|

# x = 12
# print(id(x))
# y = 12
# print(id(y))


lst = [1,2,3]
lst1 = lst

print(id(lst))
print(id(lst1))

print(lst1)
lst[1] = 'orange'
print(lst1)
print(lst)



# copy a list
lst1 = [1,2,3,4]
lst2 = lst1.copy()
print(id(lst1))
print(id(lst2))
lst2.append('sxbcdskhcb')
print(lst1)
print(lst2)

# shallow copy
# deep copy



# def name(x,y):
#     z = x+y
#     print(z)
#
# name(2,3)
#
#
#
# def name1(x,y):
#     z = x+y
#     return z
#
# print(z)