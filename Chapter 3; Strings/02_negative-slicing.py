name = "Shami"
print(name[-4 : -1])    # it means start from -4 till -1 and -1 is not included 
# it will print "ham"

# We can also do this instead of negative slicing.

print(name[1 : 4])        # It also generate the same result 


print(name[:4])  # it same as print(name[0:4]).   # if written like this. It means start from 0 till 4 and 4 is not incuded.
print(name[0:])  # it same as print(name[0:5]). # if written like this. It means start from 0 till 5 and 5 is not included.

print(name[0:5])