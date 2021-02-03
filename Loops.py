# Python has two primitive loop commands:
#
#   1.while loops
#   2.for loops


# While loop

# Syntax
# varible initialisation
# while condition:
# 	..code..
# 	..code..


# i = 1
# while i<= 5:
#     print(i)
#     i += 1

# break keyword
# i=0
# while i<5:
#     if i==3:
#     	break
#     else:
#     	print(i)
#     	i+=1


# for j in range(2):
#     i = 1
#     while i < 6:
#         print(i)
#         if i == 3:
#             print(i)
#             break
#         i += 1

# continue keyword

# i = 0
# while i < 6:
#     i += 1
#     if i == 3:
#         continue
#     print(i)
#
# # else statement
#
# i = 1
# while i < 6:
#   print(i)
#   i += 1
# else:
#   print("i is no longer less than 6")






# for loop

# A for loop is used for iterating over a sequence
# (that is either a list, a tuple, a dictionary, a set, or a string).

# The range(start,stop,step) Function
# range(6) = [0,1,2,3,4,5]


# for x in range(7):
#     print(x)

# The range() function defaults to 0 as a starting value,
# however it is possible to specify the starting value by adding a parameter: range(2, 6),
# which means values from 2 to 6 (but not including 6):

# for x in range(2, 6):
#     print(x)

# The range() function defaults to increment the sequence by 1,
# however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3)

# for x in range(24,3,-2):
#     print(x)

# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc

# fruits = ("apple", "banana", "cherry")
# for x in fruits:
#     print(x,end='%')


# Looping Through a String

# for x in "banana":
#     print(x)


# The break Statement
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     print(x)
#     if x == "banana":
#         break



# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     if x == "banana":
#         break
#     print(x)



# The continue Statement

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     if x == "banana":
#         continue
#     print(x)

# Else in For Loop

# The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
#
# for x in range(6):
#     print(x)
# else:
#     print("Finally finished!")


# Nested Loops
# A nested loop is a loop inside a loop.
# The "inner loop" will be executed one time for each iteration 
# the "outer loop":

# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]
#
# for x in adj:
#     for y in fruits:
#         print(x, y)


# The pass Statement

# for x in [0, 1, 2]:
#     pass


# cities = ['new york', 'ahmedabad','mumbai']
# capitalized_cities = []
# print("capitakized_cities: ")
# for city in cities:
# 	capitalized_cities.append(city.capitalize())
# print(capitalized_cities)
# print(cities)

# for i in range(len(cities)):
# 	cities[i] = cities[i].title()
# print(cities)


# names = ['monica gellar kszkjzsn', 'joey tribbiani','chandler bing']
# for i in range(len(names)):
#     names[i] = names[i].replace(' ', '_').title().split('_')
# print(names)


# Tag counter
# lst = ['<greeting>', 'Hello', '</greeting>','skhdj']
# count = 0
# for i in lst:
#     if i[0]=='<' and i[-1]=='>':
#         count+=1
# print(count)

# # Pattern 
# for i in range(1,5):
#     for j in range(i):
#          print(j+1, end='  ')
#     print()


# # program to display student's marks from record

# marks = {'James': 90, 'Jules': 55, 'Arthur': 77,'hkdskjs':46}
#
# for student in marks:
#     if (student == 'Arthur'):
#         print(marks[student])
#         break
# else:
#     print('No entry with that name found.')




# a = [1,2,3]
# b = [4,5,6]
# c = a + b
# print(c)


# # Building Dictionaries

book_title = ['great','expectation','great','the','adventures']
word_counter = {}
# # Method 1
# for word in book_title:
#     if word not in word_counter:
#         word_counter[word] = 1
#     else:
#         word_counter[word] += 1



# print(word_counter)

# # Method 2
# for word in book_title:
#     word_counter[word] = word_counter.get(word,0)+1
# print(word_counter)
#
# for key,value in word_counter.items():
#     print(key,end=' ')
#     print(value)

# hand = []
# card_deck = [1,2,3,4,5,6,7,8]
# while sum(hand)<=17:
#     print(sum(hand))
#     hand.append(card_deck.pop())
#     print(hand)
#     print(card_deck)
#     print(sum(hand))


#  factorial using while
# no = int(input('Enter a no: '))
# product = 1
# current = 1
# while current <= no:
#     product *= current
#     current+=1
# print(product)

# no = 5
# product =  120
# current = 6

# factorial using for

# number = int(input('Enter a no: '))
# product = 1
# for i in range(1,number+1):
#     product *= i
# print(product)

# number = 5
# product = 120
# i = 6

# Nearest Perfect Square

# limit = int(input('Enter the limit: '))
# number = 0
# nearest_perfect_square = 0
# while number**2<=limit:
#     nearest_perfect_square = number**2
#     number+=1
# print(nearest_perfect_square)

# number = 6
# nearest_perfect_square = 25



# num_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# count_odd = 2
# list_sum = 4
# i = 0
# while (count_odd<10) and (i<len(num_list)):
#     if num_list[i]%2!=0:
#         list_sum += num_list[i]
#         count_odd+=1
#         print(num_list[i])
#     i+=1
# print(count_odd)
# print(list_sum)

# i = 9
# count_odd = 5
# list_sum = 25
# 1
# 3
# 5
# 7
# 9

# range(0,stop,1)

# for i in range(10,0,-2):
# 	print(i)

