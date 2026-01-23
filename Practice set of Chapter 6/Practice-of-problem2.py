# write another program in which 50 percent. student pass

marks1 = int(input("Enter the marks of subject 1:"))
marks2 = int(input("Enter the marks of subject 2:"))
marks3 = int(input("Enter the marks of subject 3:"))

total_percentage = ((marks1 + marks2 + marks3)/300) * (100)

if(total_percentage>=50 and marks1>50 and marks2>50 and marks3>50 ):
    print("You are Pass. Best of Luck for Future.", total_percentage)


else: 
    print("You are fail. Try again next year.", total_percentage)



