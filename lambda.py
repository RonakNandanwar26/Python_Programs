# syntax
# function_name = lambda parameters: operation

# # Normally
def mul(x,y):
	z = x*y
	return z

print(mul(2,3))

mul = lambda x,y: x*y
mul(3,3)


#
# numbers = [
# [1,2,3,4],
# [2,3,4,5],
# [3,4,5,6],
# [4,5,6,7]
# ]
#
#
# def mean(num_list):
# 	return sum(num_list)/len(num_list)
#
# average =(map(mean,numbers))
# for i in average:
# 	print(i)
# print(average)
# r = range(5)
# for i in r:
# 	print(i)
# #
# #
# #
# cities = ['New york', 'LA', 'Chicago', 'Ahmedabad', 'surat']
# def is_short(name):
# 	return len(name)<=5
#
# short_cities = list(filter(is_short,cities))
# print(short_cities)
# #
# average =(map(mean,numbers))
# average = list(map(lambda x:sum(x)/len(x),numbers))
# print(average)
# short = list(filter(lambda x:len(x)<=5,cities))
# print(short)
# #
