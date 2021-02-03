# Write a Python program to display the examination schedule. (extract the date from exam_st_date).
# exam_st_date = (11, 12, 2014)
# Sample Output : The examination will start from : 11 / 12 / 2014

day = input("Enter the date")
month = input("Enter month")
year = input("Enter year")
print("class date {}/{}/{}".format(day, month, year))
