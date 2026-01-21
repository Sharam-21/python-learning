a = ["Apple", "Orange", 33, 6, 78.9, False, "Shami", "Nomi"]
print(a)

a.append("Savaiz")     # .append is used for adding a letter at the end of the list.
print(a)


l1 = [45, 98, 66, 5, 90, 10, 1]
l1.sort()            # .sort is used for sorting the list from lowest to highest numbers.
print(l1)

l2 = [22, 56, 98, 80, 1, 45, 35, 67, 11, 5]
l2.reverse()        # .reverse is used for revesing the list.
print(l2)

l3 = [22, 4, 7, 2, 56, 67, 98, 34, 0, 89, 20]
l3.insert(3,8)      # .insert is used for add a no. at specific index of the list.
print(l3)

l4 = [3, 5, 67, 89, 98, 0, 23, 56, 33, 55, 120]
l4.pop(5)           # .pop is used for delete the value or letter from the list.
print(l4)

print(l4.pop(5))     # if you write like this. it return the value at specific index only.


l5 = [33, 5, 1, 0, 77, 8, 90, 98, 67, 21, 34, 56]
l5.remove(0)       # .remove is used for removing a specific value.
print(l5)

numbers = [1, 2]
numbers.extend([3, 4, 5])       # .extend is used for extending the list.
print(numbers)

numbers1 = [1, 2, 3]
numbers1.clear()            # .clear is used for clearing the whole list.
print(numbers1)

numbers2 = [1, 2, 2, 3]
print(numbers2.count(2))     # .count is used for counting a specific value in the list.
