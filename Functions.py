# syntax
# function definition

# DRY = Do Not Repeat Yourself

# def function_name(parameters):
# 	...code...
# 	...code...
# 	...code...
#
# function call
# function_name(parameters)

# function name should not be pre defined keyword

# def operation_print():
# 	print('My name is ROnak')
#
# operation_print()


# def operation_return():
# 	return 'My name is ROnak'
#
# a = 'My name is ROnak'
# print(a)
# print(operation_return())


# Python follows DRY Priniciple  (Don't Repeat Yourself)

# Parameterized Function

def operation(y):
	y +=5
	return y


# a=14
# b = operation(a)
# print(b)

# global and local scope of variables
# z = 10
# x = 5 # global variable
# def operation_minus(y):
# 	# y is local variable
# 	global z
# 	z = 15
# 	z = x-y+z
# 	print(z)
# 	return z
#
#
# print(operation_minus(15))
# print(z)


x = 5
print(operation(x))
print(operation(10))
print(operation(12))
print(operation(10))



def addition(x,y,z):
	z = x+y+z
	print(z)
	z = x-y+z
	print(z)
	z = x*y+z
	print(z)
	z = x/y
	print(z)
	z = x%y
	print(z)
	z = x // y
	print(z)

addition(2,3,4)


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

# x = 5
#
# def plus5():
# 	x = 10
# 	x = x + 5
# 	print(x)
#
#
# plus5()
# print(x)

















