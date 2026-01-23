# Write a program which finds out whether a given name is present in a list or not. 

list = ["shami", "savaiz", "usama", "hafiz aqib", "zubair", "nomi", "ahmad"]

name = input("Enter your name :")

if(name in list):
    print("This name is present in the list. Go on and enjoy the wedding.")

else:
    print("Sorry Sir, Your name is not in the list. You cannot go inside.")    



'''Enter your name :fazal
Sorry Sir, Your name is not in the list. You cannot go inside.    

Enter your name :nomi
This name is present in the list. Go on and enjoy the wedding.'''