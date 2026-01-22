# If the names of 2 friends are same; what will happen to the program in problem 6?

a = {}
name = input("Enter your name :")
language = input("Enter your fvrt language :")
a.update({name : language})
name = input("Enter your name :")
language = input("Enter your fvrt language :")
a.update({name : language})
name = input("Enter your name :")
language = input("Enter your fvrt language :")
a.update({name : language})
name = input("Enter your name :")
language = input("Enter your fvrt language :")
a.update({name : language})

print(a)

'''it print like this : 
Enter your name :shami
Enter your fvrt language :python
Enter your name :usama
Enter your fvrt language :javascript
Enter your name :hafiz 
Enter your fvrt language :python
Enter your name :zubair 
Enter your fvrt language :java
{'shami': 'python', 'usama': 'javascript', 'hafiz ': 'python', 'zubair ': 'java'}'''


