def name(string):
	print(f"My name is {string}")


def add(a,b):
	c = a+b
	return c
name('ronak')
print('main file is ',__name__)
if __name__ == '__main__':
	print('I have a bike')
	name('Ronak')
	d = add(2,3)
	print(d)