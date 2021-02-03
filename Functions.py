# syntax
# function definition
# def function_name(parameters):
# 	...code...
# 	...code...
# 	...code...
# function call
# function_name(parameters)

# def operation_print():
# 	print('My name is ROnak')

# operation_print()

# def operation_return():
# 	return 'My name is ROnak'

# print(operation_return())



# a = operation_return()
# print(a)
# # or
# print(operation_return())

# def sum1():
# 	print('sum is jsdkajkdbs')

# sum1()

# Python follows DRY Priniciple  (Don't Repeat Yourself) 
# def operation(x):
# 	x +=5
# 	return x
# a=14
# b = operation(a)
# print(b)
# x = 5
# print(operation(x))
# print(operation(10))
# print(operation(12))
# print(operation(10))



# def addition(x,y):
# 	z = x+y
# 	print(z)

# addition(2,3)


# default arguement

# def multiply(x=2,y=1):
# 	z = x*y
# 	print(z)
#
# multiply()



# population density

# def population_density(population=1000,area=10000):
# 	density = population/area
# 	print(density)
#
# population_density()



# def week_days(day):
# 	week = day // 7
# 	days = day % 7
# 	print('no. of week is {} and days are {}'.format(week,days))
# days = int(input('Enter no. of days: '))
# week_days(days)



# Global and local variables

x = 5

def plus5():
	x = 10
	x = x + 5
	print(x)


plus5()
print(x)

















