# Object Oriented Programming
# Procedure Oriented Programming
# Functional Programming

# i = 5
# print(type(i))

# There are mainly 2 things in class
#     1.) Attribuutes -> Variables
#     2.) Behaviour -> Methods


# class Laptop:
#
#     def config(self):
#         print('i5','12gb','750gb')
#
#     def name(self):
#         print('My name is Ronak')


# a = Laptop()
# a.config()
# a.name()

# Laptop().config()
# Laptop().name()

# a = Laptop()
# Laptop.config(a)






# Constructor

class Laptop:
    def __init__(self,cpu,ram,hdd):
        self.cpu = cpu
        self.ram = ram
        self.hdd = hdd

    def get_info(self):
        print('My laptop configuration is ',self.cpu,self.ram,self.hdd)


l = Laptop('i5','12gb','750gb')
l.get_info()
m = Laptop('i9','32gb','2tb')
m.get_info()





class shirt:
    def __init__(self,name,desc,price,gender):
        self.name = name
        self.description = desc
        self.price = price
        self.gender = gender

    def info(self):
        print('shirt info',self.name,self.description,self.price,self.gender)


a1 = shirt('sakdc','sadsgkcbs','44665','Male')
a1.info()

a2 = shirt('sakhsakj','saugsaiuxh','5455','female')
a2.info()
