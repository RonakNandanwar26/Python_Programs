# zip

#  zip returns iterator that combines multiple iterables into
# one sequence of tuples
# ('a',1),('b',2),('c',3)

# letters = ['a','b','c']
# nums = [1,2,3]
# lst = [4,5,6]
# print(zip(nums,letters))
#
# for letters,nums,lst in zip(letters,nums,lst):
# 	print(letters,nums,lst)

# # unzip

# lst = [('a',1),('b',2),('c',3)]
# letter,num = zip(*lst)
# print(letter,num)




# Enumerate

# Enumerator is a built in function that returns an iterator
# of tuples containing indices and value of list

# letters = ['a','b','c','d','e','f']
# for i,letter in enumerate(letters):
# 	print(i,letter)



# use zip to write for loop that creates string specifying the label and 
# co-ordinates of each point and appends it to the list points.
# each string should be formatted as 'label:x,y,z'

x_coord = [23,4,5]
y_coord = [56,3,4]
z_coord = [12,5,6]
labels = ['a','b','c']

points = []

# for point in zip(labels,x_coord,y_coord,z_coord):
# 	print(point)

for point in zip(labels,x_coord,y_coord,z_coord):
	points.append('{}:{},{},{}'.format(*point))

print(points)
for i in points:
	print(i)



# # zip to create dictionary

cast_names = ['barney','Robin','Ted']
cast_heights = [72,68,90]
cast = dict(zip(cast_names,cast_heights))
print(cast)
# for n,h in cast:
#     print(n,h)
# # zip to create tuple
# cast_names = ['barney','Robin','Ted']
# cast_heights = [72,68,90]
# cast = tuple(zip(cast_names,cast_heights))
# print(cast)

# # zip to create list
# cast_names = ['barney','Robin','Ted']
# cast_heights = [72,68,90]
# cast = list(zip(cast_names,cast_heights))
# print(cast)


# unzip cast tuple 

# cast = (('barney', 72), ('Robin', 68), ('Ted', 90))
# name,height = zip(*cast)
# print(name,height)
# print(height)

# Transpose matrix using zip

data = ((0,1,2),(1,2,3),(3,4,5))
print(data)
data_transpose = tuple(zip(*data))
print(data_transpose)



names = ['barney','Robin','Ted']
heights = [72,68,90]

for i,name in enumerate(names):
	names[i] = name + " " + str(heights[i])

print(names)