# Write a Python program to display the current date and time.
# Sample Output :
# Current date and time :
# 2014-07-05 14:34:14

import datetime
now = datetime.datetime.now()
print ("Current date and time : ", now)


# Write a Python program to calculate number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)


from datetime import date
f_date = date(2014,7,2)
l_date = date(2014,7,11)
num_days = l_date - f_date
print(num_days)