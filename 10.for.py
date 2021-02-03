# Write a Python program to concatenate all elements in a list into a string and return it.

lst = [1,4,6,7,8]
number = str()
for num in lst:
    number += str(num)
print(number)


numbers = [
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958,743, 527
    ]

for num in numbers:
    if num == 237:
        break;
    if num%2==0:
        print(num)