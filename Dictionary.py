# Dictionary
# A dictionary is a collection which is unordered, changeable and indexed.
# In Python dictionaries are written with curly brackets, and they have keys and values.
# a = {1,2}
# print(type(a))
#
# dct = {
#     'bio': 1+7j,
#     'name' : 'Ronak',
#     'age' : 21
# }
# print(dct['name'])
# print(dct)
#
# Accessing items
# x = dct['name']
# print(x)
#
# # change value
# dct['bio'] = 'sahgksabls'
# print(dct)
# dct[21] ='sdfdhfd'
# print(dct)

# # print only dictionary keys
# print(dct.keys())
# #
# # print only dictionary values
# print(dct.values())
#
# # check wheather a keys is present in dict or not # membership operator
# print('name' in dct)
# print('address' in dct)
# To check values
# print('name' in dct.values())
# # #  Dictionary length
# print(len(dct))
#
# # # Add items
# dct['address'] = 'sdjnkjdsnbfl'
# print(dct)
#
# # remove items
# dct.pop('address')
# print(dct)
#
# # popitem() method to remove element from dictionary
# dct.popitem()
# print(dct)
# dct.popitem()
# print(dct)
#
# # remove using del
# del dct['name']
# print(dct)
#
# del dct
# print(dct)
#
# # we can also delete whole dictionary using del
thisdict =	{
  "brand": ["Ford",'kdsjsd'],
  "model": "Mustang",
  "year": 1964
}
# print(thisdict)
# # del thisdict
# print(thisdict)

# empty type creation
# s = {1,2,3}
# s.clear()
# print(s)
#
# dct.clear()
# print(dct)


# a = set()
# print(a)
# a.add(1)
# print(a)
# print(type(a))

# c = {}
# print(c)
# print(type(c))
#
# b = ()
# print(type(b))
#
# a =[]
# print(type(a))


# # to clear the dictionary
# thisdict.clear()
# print(thisdict)
#
# # copy a dictionary
# deep copy
# shallowdct = thisdict
# print(id(shallowdct))
# print(id(thisdict))
# print(id(thisdict))
# mydict = thisdict.copy()
# print(mydict)
# print(id(mydict))
#
# # shallow copy
# mydict = thisdict
# print(id(mydict))
# print(id(thisdict))
#
# # # Nested dictionary
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
#
print(myfamily['child1'])
print(myfamily['child1']['name'])
print(myfamily['child1']['name']['middlename'])

# print(myfamily.get('child1').get('name').get('surname'))
#
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
#
myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily['child2']['year'])
#
#
# #  get method gives value
# x = myfamily.get('child2').get('name')
# print(x)

# # items
z = myfamily.items()
print(z)
#
# # update method
# myfamily['child4']='sakjhsdkjwb'
# print(myfamily)
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car['color'] = 'red'
print(car)
car.update({"color": "White",'model':'asbckj','address':'kjsdksd','std':'shbdskj'})
# # # #
print(car)