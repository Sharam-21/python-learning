'''Write a program to find whether a given username contains less than 10
characters or not.'''



username = input("Enter your username :")

if(len(username) <10):
    print("Thanks for giving the username, that contain less than 10 characters.")

else:
    print("Try again. Enter username that have less than 10 characters.")    


'''Enter your username :shami
Thanks for giving the username, that contain less than 10 characters.    

Enter your username :sharam shabbir
Try again. Enter username that have less than 10 characters.'''