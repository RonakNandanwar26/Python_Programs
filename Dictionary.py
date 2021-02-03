# Dictionary
# A dictionary is a collection which is unordered, changeable and indexed.
# In Python dictionaries are written with curly brackets, and they have keys and values.


dct = {
    'bio' : 'jd',
    'name' : 'Ronak',
    'age' : 21
}
print(dct)

# Accessing items
x = dct['bio']
print(x)

# change value
dct['bio'] = 'sahgksabls'
print(dct)
dct[21] ='sdfdhfd'
print(dct)

# print only dictionary keys
print(dct.keys())

# print only dictionary values
print(dct.values())

# check wheather a keys is present in dict or not # membership operator
print('name' in dct)
print('address' in dct)

# #  Dictionary length
print(len(dct))

# # Add items
dct['address'] = 'sdjnkjdsnbfl'
print(dct)

# remove items
dct.pop('address')
print(dct)

# popitem() method to remove element from dictionary
dct.popitem()
print(dct)
dct.popitem()
print(dct)

# remove using del
del dct['name']
print(dct)

# del dct
# print(dct)

# we can also delete whole dictionary using del
# thisdict =	{
#   "brand": ["Ford",'kdsjsd'],
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict)
# del thisdict
# print(thisdict)

# to clear the dictionary
# thisdict.clear()
# print(thisdict)

# copy a dictionary
# mydict = thisdict.copy()
# print(mydict)

# copy using dict() method
# mydict = dict(thisdict)
# print(mydict)


# Nested dictionary
myfamily = {
  "child1" : {
    "name" : {'surname':'skhdsl','middlename':'xmbdskbdk'},
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily['child1']['year'])

# other method
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily['child2']['year'])


#  get method gives value
# x = myfamily.get('child2').get('name')
# print(x)

# items
z = myfamily.items()
print(z)

# update method
myfamily['child4']='sakjhsdkjwb'
print(myfamily)
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car['color'] = 'red'
print(car)
car.update({"color": "White",'model':'asbckj','address':'kjsdksd','std':'shbdskj'})
#
print(car)