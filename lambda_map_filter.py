# mul = lambda x=3,y=4: x*y
# print(mul(3))




numbers = [
[1,2,3,4],
[2,3,4,5,5,6],
[3,4,5,6],
[4,5,6,7]
]


# def mean(num_list):
# 	return sum(num_list)/len(num_list)

average = list(map(lambda num_list: sum(num_list)/len(num_list),numbers))
for i in average:
	print(i)
print(average)



cities = ['New york', 'LA', 'Chicago', 'Ahmedabad', 'surat']
def is_short(name):
	return len(name)<=5

short_cities = filter(lambda name: len(name)<5 ,cities)
print(short_cities)

for i in short_cities:
	print(i,end=' ')

# short = list(filter(lambda x:len(x)<5,cities))

# print(short)