


class Person:
	def __init__(self,name,age):
		self.name = name
		self.age = age

	def myfun(self):
		print('my name is '+ self.name)


p = Person('John',23)
print(p.name,p.age)
p.myfun()
p.age = 40
# print(p.age)
# del p.age
# print(p.age)
q = Person('Faizan',20)
print(q.name,q.age)
