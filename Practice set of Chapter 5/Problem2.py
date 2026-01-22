'''Write a program to input eight numbers from the user and display all the unique
numbers (once).'''

a = set()

b = input("Enter a number:")
a.add(int(b))
b = input("Enter a number:")
a.add(int(b))
b =input ("Enter a number:")
a.add(int(b))
b = input("Enter a number:")
a.add(int(b))
b = input("Enter a number:")
a.add(int(b))
b = input("Enter a number:")
a.add(int(b))
b = input("Enter a number:")
a.add(int(b))
b = input("Enter a number:")
a.add(int(b))
b = input("Enter a number:")
a.add(int(b))

print(a)      
'''Enter a number:2
Enter a number:3
Enter a number:4
Enter a number:5
Enter a number:2
Enter a number:3
Enter a number:4
Enter a number:5
Enter a number:5
{2, 3, 4, 5}'''



z = set()
y = input("Enter no. : ")
z.add(int(y))
y = input("Enter no. : ")
z.add(int(y))
y = input("Enter no. : ")
z.add(int(y))

print(z)

'''it prints: Enter no. : 1
Enter no. : 2
Enter no. : 2
{1, 2}'''
