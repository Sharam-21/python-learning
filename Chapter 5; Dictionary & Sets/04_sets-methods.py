a = {22, 56, 21, 67, 98, 0, 45, 34}
a.add(445)          # .add is used for adding a no. in the set.
print(a, type(a))     # it prints: {0, 98, 67, 34, 45, 21, 22, 56, 445} <class 'set'>

a.update([5, 6, 7])        # .update is used for updating the set and add these no. also.
print(a, type(a))     # it prints: {0, 98, 67, 34, 5, 6, 7, 45, 21, 22, 56, 445} <class 'set'>

a.remove(6)         # .remove is used for removing a specific no. from the set.
print(a, type(a))    # it prints: {0, 98, 67, 34, 5, 7, 45, 21, 22, 56, 445} <class 'set'>

a.pop()           # .pop removes a random value.
print(a)      # it prints : {98, 67, 34, 5, 7, 45, 21, 22, 56, 445}

a.discard(10)      # .discord it Removes an element (no error if not found), if element is not in the set.
print(a)         # it prits: {98, 67, 34, 5, 7, 45, 21, 22, 56, 445}

a.clear()     # .clear is used for clear the whole set.
print(a, type(a))      # it prints : set() <class 'set'>





