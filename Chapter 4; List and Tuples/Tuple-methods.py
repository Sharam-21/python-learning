a = (22, 33, 55, 67, 22, 21, 3, 4, 6, 9, 0)
b = a.count(22)
print(b)
print(a.count(22))         
                       # Both methods are same. Bcz .count is used for count a specific value. How many times this value comes in the tuple.
t = (10, 20, 30, 20)
print(t.index(20))      # .index is used for finding the index od specific number.

student = ("Ali", 20, "CS")
print(student[0])   # Access element        # print the value that exist at specific index. 

print(len(t))
# len is used for getting the length of the tuple.
print(max(t))
# max  is used for getting the maximum value of the tuple.
print(min(t))
# min is used for getting the minimum value of the tuple.
print(sum(t))
# sum is used for the adding the all numbers of the tuple and return the answer of the sum.

t1 = (1, 2) 
print(t1 * 3)    # It return tuple value 3 times.

t2 = (1, 2, 3)
print(2 in t2)
print(5 not in t2)    # It helps to find a specific value is available in the tuple or not.





