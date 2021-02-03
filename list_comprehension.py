cities = ['ahmedabad','Vadodara','navsari','surat']

# Normally
# capitalise_cities = []
# for city in cities:
# 	capitalise_cities.append(city.capitalize())
#
# print(capitalise_cities)

# list comprehension
# capitalise_cities = [city.capitalize() for city in cities]
# print(capitalise_cities)
#
# # Normally
lst = []
# for x in range(5):
# 	if x%2 == 0:
# 		lst.append(x**2)
# print(lst)
#
# # list comprehension
# squares = [x**2 for x in range(5) if x%2 == 0]
# print(squares)
# # # Normally
for x in range(9):
	if x%2 == 0:
		print(x**2)
	else:
		print(x+3)
# # List comprehension
square = [x**2 if x%2 == 0 else x+3 for x in range(9)]
print(square)
#
# # square = [x**2 if x%2==0 else x+3 for x in range(9)]
#
square = [x**2 for x in range(7) if x%2!=0]
print(square)