'''Write a program to create a dictionary of Urdu words with values as their English
translation. Provide user with an option to look it up!'''

words = {
        "pani": "Water",
        "kalam" : "Pen",
        "katab" : "Book", 
        "ghar" : "House"
}
user = input("Enter the name :")
print(words[user])
# it prints like : Enter the name :ghar.    House



result = {
    "Shami" : "100",
    "Savaiz" : "99",
    "Nomi" : "98",
    "Hafiz" : "97",
    "Usama" : "96",
    "Zubair" : "95"
}

User2  = input ("Enter name to get reult :")
print(result[User2])

# it prints like : Enter name to get reult :Usama.        96
