# Object Oriented Programming
# Procedure Oriented Programming
# Functional Programming
#
# i = 50.0
# print(type(i))

# There are mainly 2 things in class
#     1.) Attribuutes -> Variables
#     2.) Behaviour -> Methods

#
# class aptop:
#     pass
#
# a = aptop()
# a.name = 'Ronak'
# b = aptop()
# b.age = 22
# print(a.name)
# print(b.age)

# class Laptop:
#     def __init__(self):
#         print('in init')
#
#     def config(self):
#         print('i5','12gb','750gb')
#
#     def name(self):
#         print('My name is Ronak')
# #
# #
# a = Laptop()
# a.config()
# a.name()
#
# Laptop().config()
# Laptop().name()

# a = Laptopfig()
# Laptop().name()
# Laptop.config(a)






# Constructor
#
# class Laptop:
#     def __init__(self,cpu,ram,hdd):
#         self.cpu = cpu
#         self.ram = ram
#         self.hdd = hdd
#         print('in constructor')
#
#     def get_info(self):
#         print('My laptop configuration is ',self.cpu,self.ram,self.hdd)
# #
# #
# l = Laptop('i5','12gb','750gb')
# l.get_info()
# m = Laptop('i9','32gb','2tb')
# m.get_info()
#




# class shirt:
#     def __init__(self,name,desc,price,gender):
#         self.name = name
#         self.description = desc
#         self.price = price
#         self.gender = gender
#
#     def set_name(self,name,desc,price,gender):
#         self.name = name
#         self.description = desc
#         self.price = price
#         self.gender = gender
#
#     def get_shirt_info(self):
#         print('shirt info',self.name,self.description,self.price,self.gender)
#
#
# a1 = shirt('sakdc','sadsgkcbs','44665','Male')
# a1.info()
#
# a2 = shirt('sakhsakj','saugsaiuxh','5455','female')
# a2.info()
#
# a2.set_name('casual shirt','zxcnljsd','456','Male')
# a2.info()




#
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def get_person_info(self):
#         print(f"Name is {self.name} and age is {self.age}")
#
#     def compare(self,other):
#         if self.age == other.age:
#             return True
#         else:
#             return False
#
# p1 = Person('Ronak',22)
# p2 = Person('sdkhc',22)
#
# if p1.compare(p2):
#     print('age is same')
# else:
#     print('age is not same')




# Types of variable in OOPs
# Instance variable
# Class varible(static variable)

# class Car:
#     wheel = 4
#     def __init__(self,name,type):
#         self.name = name
#         self.type = type
#
#     def get_car_info(self):
#         print(self.name,self.type,self.wheel)
#
# c1 = Car('BMW','SUV')
# c2 = Car('Audi','sedan')
#
# c1.get_car_info()
# c2.get_car_info()
#
# c1.wheel = 5
# c1.get_car_info()
#
# Car.wheel = 6
#
# print(c1.wheel)
#
# print(c2.wheel)
