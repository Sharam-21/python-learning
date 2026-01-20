name = "Sharam"
print(len(name))         # it prints the length of the string. That is 6.

print(name.endswith("ram"))       # it prints True bcz the name ends with 'ram'
print(name.endswith("ara"))       # it prints False bcz the name ends with 'ram'

# .endswith function is ised for confirm the string is ends wirth this number, name or not.

print(name.startswith("Sha"))       # it prints True bcz the name starts with 'Sha'
print(name.startswith("ram"))      # it prints False bcz the name starts with 'Sha'

# .startswith function is ised for confirm the string is start wirth this number, name or not.

b = "shami"
print(b.capitalize())     # .capitalize. This function capitalize the first alphabet of the string.
# This returns 'Shami'

text1 = "HELLO  I AM SHAMI"
print(text1.lower())     # .lower. This function lower the all alphabets of the string.

text2 = "hello i am shami"
print(text2.upper())      # .uppper. this function upper the all alphabets of the string.

text3 = "  hello  "
print(text3.strip())     # .strip. This function is used for removing the space from start and end.

text4 = "hello world"
print(text4.replace("world", "Python"))
# .replace. This function is used for replacing the letter to another letter in the string.

text5 = "apple,banana,orange"
print(text5.split(","))    # .spilt. This function is used for change string into list.

fruits = ["apple", "banana", "orange"]
print(", ".join(fruits))        # .join. This function is used for change the list into string.

text6 = "banana"
print(text6.count("a"))     # .count. This function is used count the specific alphabet in the string.

text7 = "Hello"
print(text7.isalpha())     # .isalpha. This function is used for confirm the string is containg all letters.

text8 = "1234"
print(text8.isdigit())     # .isdigit. This function is used for confirm the string is containing all numbers.


text9 = "my name is sharam"
print(text9.title())     # .tittle. This function capitalize the first letter of each word that in the string.

text10 = "My name is Sharam"
print(text10.find("name"))    # .find. This function find the specific letter and tell the index, where this letter starts.
# it returns 3.





