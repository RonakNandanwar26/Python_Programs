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



# Accessesor ->getter
# Mutator ->setter


# Types of Method
# 1. instance method
# 2.class method
# 3. static method


#
# class Student:
#     school = 'Silverwing'
#
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
#
#     def get_student_info(self):
#         print(self.name)
#         print(self.marks)
#
#     @classmethod
#     def get_school(cls):
#         print(cls.school)
#
#     @staticmethod
#     def info():
#         print('This is school')
#
#
# s = Student('Ronak',45)
# s.get_student_info()
# s.get_school()
# s.info()


# Concepts of OOPs Programming
# 1. Encapsulation
# 2. Abstraction
# 3. Inheritance
# 4. Polymorphism




# Inheritance

# Parent class -> Super class
# child class -> sub class

# single Inheritance
# class A:
#     def feature1(self):
#         print('This is feature 1')
#
# class B(A):
#     def feature2(self):
#         print('This is feature 2')
#
# a = A()
# a.feature1()
# b = B()
# b.feature2()
# b.feature1()


# Multilevel Inheritance

# class A:
#     def feature1(self):
#         print('This is feature 1')
#
# class B(A):
#     def feature2(self):
#         print('This is feature 2')
#
# class C(B):
#     def feature3(self):
#         print('This is feature 3')
#
#
# a = A()
# a.feature1()
# b=B()
# b.feature1()
# b.feature2()
#
# c = C()
# c.feature1()
# c.feature2()
# c.feature3()


# Multiple Inheritance

# class A:
#     def feature1(self):
#         print('This is feature 1')
#
# class B:
#     def feature2(self):
#         print('This is feature 2')
# class C(A,B):
#     def feature3(self):
#         print('This is feature 3')
#
#
# a=A()
# a.feature1()
# b=B()
# b.feature2()
# c =C()
# c.feature1()
# c.feature2()
# c.feature3()
#
#


# hierarchical inheritance
# class A:
#     def feature1(self):
#         print('feature1')
#
# class B(A):
#     def feature2(self):
#         print('feature2')
#
# class C(A):
#     def feature3(self):
#         print('feature3')
#
# class D(A):
#     def feature4(self):
#         print('feature4')
#
#
# c = C()
# c.feature1()


# hybrid inheritance

# class A:
#     def feature1(self):
#         print('feature1')
#
# class B(A):
#     def feature2(self):
#         print('feature2')
#
# class C(A):
#     def feture3(self):
#         print('feature3')
#
# class D(B,C):
#     def feature4(self):
#         print('feature4')
#
# d = D()
# d.feature1()


# polymorphism

# class PyCharm:
#     def execute(self):
#         print('runnig A')
#
# class VsCode:
#     def execute(self):
#         print('runing B')
#
# class program:
#     def code(self,ide):
#         ide.execute()
#
# ide = PyCharm()
# p = program()
# p.code(ide)

