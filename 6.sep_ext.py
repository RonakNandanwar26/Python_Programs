# Write a Python program to accept a filename from the user and print the extension of that.
# Sample filename : abc.java
# Output : java


f_name = input('Enter a file name:' )
f_name = f_name.split('.')
print(f_name[-1])