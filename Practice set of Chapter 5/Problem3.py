# Can we have a set with 18 (int) and '18' (str) as a value in it? 

s = {18, "18"}
s.add(17)
s.add("17")
print(s, type(s))

# it print like : {'18', 17, 18, '17'} <class 'set'>