a = 5.0
print(type(a))
#
# float
# # syntax
# # class classname:
# # 	code
#
#
# class Person:
# 	pass

# a = Person()
# b = Person()
# # print(type(a))
# a.name = 'Ronak'
# print(a.name)
# a.age = 21
# print(a.age)
# a.height = 6
# print(a.height)
# b.height = 5
# print(b.height)


# class Person:
#     def __init__(self):
#         self.name = 'ROnak'
#
# a = Person()
# b =Person()
# print(a.name)
# print(b.name)



class person:
	def __init__(self,name,age,height):
		self.name = name
		self.age = age
		self.height = height
#
#
#
a = person('Ronak',21,6)
b = person('Mayur',25,7)
print(a.name)
print(a.age)
print(a.height)
print(b.name)
print(b.age)
print(b.height)



b = person('Ronak',21,6)
print(type(b))

# a = 5
# print(type(a))