# Tuple
# collection of ordered and immutable elements
#
# Tuple Identification
# a = (1,2,'orange',4.5,'a')
# # Access the tuple values
# print(a[4])
# # Indexes and Ranges of Indexes
# print(a[::-2])

# a[2] = 5
# print(a)

# #change the values of tuple
# lst = list(a)
# print(lst)
# lst[1] = 9
# print(lst)
# a = tuple(lst)
# print(a)

# # length of tuple
# print(len(a))




# #create tuple with one item, you need to add a comma unless python will not recognize it as tuple
# a = (1,)
# print(a)
# print(type(a))
# # remove items
# tuple is immutable 
#
# Join 2 tuples using + operators
# c = a + ('a',1,1,1,1,2)
# print(c)
# check if item exist
# print(7 not in a)


# # count method, TO count particular element in the tuple
# c = c.count(1)
# print(c)
# #index method
a = ('a','b','c')
print(a)
# c = a.index('c')
# print(c)
# #

# a = [1,2,2]
# print(a.count(1))






# set
# it is unordered and unidexed, so you cannot be sure in 
# which order the item will appear
a = {1, 2,1, 'a', 'b','b'}
print(a)
# can not Access items using index

# membership operator
print('c' in a)
# # change items
# #  In set once set is creted you cannot change its items but you can add or update items
# lst = list(a)
# print(lst)
# print(set(lst))
#
# # Add itemadds
a.add(3)
print(a)
# # # update items   Add multiple items
a.update(['a',2,4,1])
print(a)
# # length of set
print(len(a))
print(a)
#
# # pop

a.pop()
print(a)
#
a.pop()
print(a)

# # clear
a.clear()
print(a)
a.add(1)
print(a)
# # # join two sets union
set1 = {1,2,3}
set2 = {'a','b','c',3}
set3 = set2.union(set1)
print(set3)
print(set1)
print(set2)
# del set2
# print(set2)


lst = [1,2,3,4,5,6,3,4,5,6,3,4,5,6,4,3,2,3,4,5,4,3,3,4,5,6,6,7,5,4,2,2,4,5,6,7,5,4,3]
a = set(lst)
print(a)




# lst = (2,6,4,9,2,1)
# print(type(sorted(lst)))


# lst = [1,2,3]
# lst.clear()
# print(lst)
#
# s = set(lst)
# print(s)
#
# s = []
# print(type(s))
#
# s = {}
# print(type(s))











#
# x = 1
# print(type(x))
# print('Ther is '+str(x))
# print(type(str(x)))
# print(float(x))
# print(type(float(x)))
# print(complex(x))
# print(type(complex(x)))
# print(x)

# x = '1298434374370'
# print(type(x))
# print(int(x))
# y = 'a'
# print(int(y))

