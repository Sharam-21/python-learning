# If languages of two friends are same; what will happen to the program in problem 6?

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
Enter your name :zubair 
Enter your fvrt language :java
Enter your name :shami  
Enter your fvrt language :Javascript
{'shami': 'Javascript', 'usama': 'javascript', 'zubair ': 'java'}'''

# bcz we used update method thats why it update at last python to javascript language of shami