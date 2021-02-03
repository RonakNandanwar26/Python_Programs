# Tuple
# collection of ordered and immutable elements
#
# Tuple Identification
a = (1,2,'orange',4.5,'a')
# # Access the tuple values
# print(a[4])
# # Indexes and Ranges of Indexes
# print(a[1:3:2])

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
print(len(a))
# #create tuple with one item, you need to add a comma unless python will not recognize it as tuple
b = ('dskjncdskj',)
# print(b)
# print(type(b))

# # remove items
# tuple is immutable 
#
# # Join 2 tuples using + operators
c = a + b + ('a',1,1,1,1,2)
print(c)
# # check if item exist
print(1 in a)
# # count method, TO count particular element in the tuple
c = c.count(1)
print(c)
# #index method
c = a.index(4.5)
print(c)
# #

a = [1,2,2]
print(a.count(2))





# set
# it is unordered and unidexed, so you cannot be sure in 
# which order the item will appear
# a = {1, 2,1, 'a', 'b'}
# print(a)
# can not Access items using index
# print(a[1])
# membership operator
# print(1 not in a)
# # change items
# #  In set once set is creted you cannot change its items but you can add or update items
# lst = list(a)

# set(lst)
#
# # Add items
# a.add(3)
# print(a)
# # # update items   Add multiple items
# a.update([1,2,4])
# print(a)
# # length of set
# print(len(a))
# print(a)
#
# # pop
# a.pop()
# print(a)

# a.pop()
# print(a)
# b = tuple()
# print(b)
# # clear
# a.clear()
# print(a)
# a.add(1)
# print(a)
# # join two sets union
# set1 = {1,2,3}
# set2 = {'a','b','c'}
# set3 = set1.union(set2)
# print(set3)
# print(set1)
# print(set2)
# del set2
# print(set2)


# lst = [1,2,3,4,5,6,3,4,5,6,3,4,5,6,4,3,2,3,4,5,4,3,3,4,5,6,6,7,5,4,2,2,4,5,6,7,5,4,3]
# a = set(lst)
# print(a)




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