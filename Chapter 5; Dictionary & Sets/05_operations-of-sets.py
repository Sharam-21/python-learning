s = {1,8,2,3}

print(len(s))    # len is used for getting the lenth of the set. it prints: 4

s.remove(8)      # .remove is used for remove a specific element from the set.
print(s, type(s))     # it prints : {1, 2, 3} <class 'set'>

a = {1, 4, 6, 8, 98, 65, 67, 21, 34, 55, 0}
b = { 33, 66, 77, 89, 78, 45, 54, 90}
print(a.union(b))   # .union is used for combine the 2 sets and given all elements of both sets.
# it prints: {0, 1, 65, 67, 4, 66, 6, 8, 77, 78, 21, 89, 90, 33, 98, 34, 45, 54, 55}

c = {1, 3, 5, 7}
d = {2, 4, 6, 8}
print(c.union(d))   # it prints: {1, 2, 3, 4, 5, 6, 7, 8}

e = {2, 4, 6, 8, 0, 10, 22, 44}
f = {1, 3, 2, 5, 6, 7, 9, 11, 33}
print(e.intersection(f))      # .intersection is given the common values of the both sets.
# it prints : {2, 6}

g = {1, 2, 3, 4, 5}
h = {2, 5, 0, 6, 7}
print(g.difference(h))      # .difference is used for Elements in first set but not second.
# it prints : {1, 3, 4}

i = {1, 2, 3, 4, 5}
h = {2,3}
print(i.issubset(h))      # .issubset is used for the values of set i is available in the set h . if yes it returns True, if not it returns False.
# it prints : False.  bcz all elements of set i is not present in the set h.
print(h.issubset(i))         # it prints: True. Bcz all elements of set h is present in the set i.

print(i.issuperset(h))    # .issuperset is return True or False. if all of set h is present in the set it return True, if not it returns FAlse.
# it prints: True. Bcz all elements of set h are present in set i.
print(h.issuperset(i)) 
# it prints : FAlse. Bcz all elements of set i is not present in the set h.