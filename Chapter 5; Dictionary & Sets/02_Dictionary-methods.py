fruits = {
    "Mango" : 100,
    "Bannana" : 70,
    "cherry" : 250,
    "watermelon" : 50,
    "orange": 80
}

print(fruits.items())
# .items is give the value in the form of list.
#  like this: dict_items([('Mango', 100), ('Bannana', 70), ('cherry', 250), ('watermelon', 50), ('orange', 80)])

print(fruits.keys())
# .keys  give the key value of prices.
# like this : dict_keys(['Mango', 'Bannana', 'cherry', 'watermelon', 'orange'])

print(fruits.values())
# .value is print the value of all fruits in the dictionary.
# like this: dict_values([100, 70, 250, 50, 80])

fruits.update({"watermelon": 90 , "pineapple" : 1500}) 
# .update is used for updating the specific dictionary letter or add another one also.
print(fruits)
# now it shows like this : {'Mango': 100, 'Bannana': 70, 'cherry': 250, 'watermelon': 90, 'orange': 80, 'pineapple': 1500}

print(fruits.get("grapes"))
# .get is return the value of given name.
# if the name is not in the dictionary it returns : None.

print(fruits.get("orange"))
# in this case it returns : 80. Bcz this is existing name in the dictionary.

'''print(fruits.get("apple"))    Print None
print(fruits["apple"])           it returns an error.''' 

fruits.popitem()
# .pop item Removes the last inserted key–value pair.
print(fruits)

fruits.pop("watermelon")
# .pop is used for Removes a key and returns its value.
print(fruits)


