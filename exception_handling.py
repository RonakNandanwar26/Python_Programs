# try__except__else__finally


# try: It is only mandatory clause in exception handling.try runs first in 
# 	try__except

# except: if python runs into an exception, then code present in except
# 		will run.

# else:  if try is successfully executed then after execution of try block else part
# 		will execute.

# finally:  this part always runs.


# x = int(input('Enter a number'))
# print(x)

# try:
# 	x = int(input('Enter a number'))
# 	print(x)
# except:
# 	print('Enter a valid integer number')


# try:
# 	x = int(input('Enter a number: '))
# 	print(x)
# except:
# 	print('Enter a valid number')
# else:
# 	print('sdhbsdkjns')
# finally:
# 	print('your task is done!')
# # --------------------------------------------

# x = int(input('Enter a number'))
# y = int(input('enter a number'))
# z = x/y
# print(z)


# try:
# 	x = int(input('Enter a number'))
# 	y = int(input('enter a number'))
# 	z = x/y
# 	print(z)
# except ValueError:
# 	print('Enter a valid integer number')
# except KeyboardInterrupt:
# 	print('You pass the keyboard interrupt')
# except ZeroDivisionError:
# 	print('You are dividing number by zero')



try:
	x = int(input('Enter a number'))
	y = int(input('enter a number'))
	z = x/y
	print(z)
except (ValueError,ZeroDivisionError,KeyboardInterrupt):
	print('not a valid number or you are dividing value by 0 or you pass the keyboard interrupt')

