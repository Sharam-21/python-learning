'''Create an empty dictionary. Allow 4 friends to enter their favorite language as
value and use key as their names. Assume that the names are unique.'''

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

'''It print like this : Enter your name :Shami
Enter your fvrt language :Python
Enter your name :Usama
Enter your fvrt language :Javascript
Enter your name :Aqib 
Enter your fvrt language :Java
Enter your name :Zubair 
Enter your fvrt language :C++
{'Shami': 'Python', 'Usama': 'Javascript', 'Aqib ': 'Java', 'Zubair ': 'C++'}'''