a = int(input("Enter your age:"))

if(a%2==0):                      # this if is independent if.
    print("Your entered a even number")

if(a>=18):
    print("Your age is above the consent.")

elif(a==0):
    print("You entered 0, which is invalid age.")

elif(a<0):
    print("You entered negative age, which is not valid.")

else:
    print("You are not 18, you cannot get this offer")
    
                    