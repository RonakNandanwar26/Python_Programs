# List
# It is a combination of any datatype elements, indexed, Mutable
a = [1,'sdh','6',1+2j]
print(a[2])
a.remove(1)
print(a)
del a[0]
print(a)
a = a+[5,5,5]
print(a)
a.append('sksdb')
print(a)
a.insert(2,'askbxsakjxbkjas')
print(a)
a.pop()
print(a)
print(a.count(5))
# a.clear()
# print(a)
b = a.copy()
print(id(a))
print(id(b))
b.append('abcd')
print(a)
print(b)
a.extend(['xksc',56,87])
print(a)
print(a.index('6'))
b = [4,5,7,3,8]
print(len(a))




# Write a Python program which accepts a sequence of comma-separated numbers from user
# and generate a list and a tuple with those numbers.
# Sample data : 3, 5, 7, 23
# Output :
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23')


# num = input('Enter comma separated numbers: ' )
# num = num.split(',')
# lst = list(num)
# tup = tuple(num)
# print(lst)
# print(tup)