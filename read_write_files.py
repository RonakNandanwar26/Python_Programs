# reading and writing in files

# reading the file
# syntax:
# object_name = open('file name.extension', mode) 

# f = open('scrapping_tool.txt', 'r')  # scrapping tool.txt is fle name which yo want to open and
# 									 # 'r' stands for  read mode which is optional parameter
# 									 # 'w' stands for write mode
# file_data = f.read()
# print(file_data)
# f.close()




# writing the file

# f = open('scrapping.py','w')
# f.write(input('enter something :'))
# f.close()
#
# f = open('bsdcjbsljcbsljcbsdl.txt','w')
# f.write('jbskbackjbsjbcjasbcjsbkjcbsjcbkjsbcljsabcljasbclj')
# f.close()

# # if there is no file available in your system you named,
# #  it will automatically create it for you.


# # too many open files

# files = []
# for file in range(10000):
# 	files.append(open('scrapping_tool.txt','r'))
# 	print(file+1)



# #  using with

# Python provides special syntax that autoclose the file for you, once you're finish using it.
# f = open('filename',mode)

# with open('file name', mode) as objectname:
# 	code


# with open('scrapping_tool.txt','r') as f:
# 	file_data = f.read()
#
# print(file_data)

# 
# # The 'with' keyword allows you to open a file,
# # do operation on it and automatically close it, 
# # after the intended code is executed.
#
# def create_cast_list(filename):
#
# 	with open(filename) as f:
# 		for line in f:
# 			name = line.split()
#
# 		return name


# cast_list = create_cast_list('scrapping_tool.txt')
# print(cast_list)
#
# for word in cast_list:
# 	print(word)


# # append something in file

# with open('scrapping_tool.txt','a') as f: # a stands for append
# 	f.write('This is appended new line ')
#
#
# with open('scrapping_tool.txt', 'r') as f:
# 	print(f.read())



# # copy a file 

with open('scrapping_tool.txt','r') as readfile:
	with open('c_scrapping_tool.txt','w') as writefile:
		for line in readfile:
			writefile.write(line)


with open('c_scrapping_tool.txt','r') as f:
	print(f.read())



