birthdaydic = {
    "Peter": "01/02/2000",
    "Diane": "01/02/1999",
    "Philip": "01/02/1995",
    "Father": "01/02/1972",
    "Mother": "01/02/1975",
    "GodFather": "01/02/1970",
    "GodMother": "01/02/1970",
    "Granfather": "01/02/1940"
    }
print("Welcome to the birthday dictionary. We know the birthday of the following people: \n")
for key, value in birthdaydic.items():
    print(key)
user = input("What birthday date do you wanna know?\n")
if user in birthdaydic:
    print(f"{user} were born in {birthdaydic[user]}!")
else:
    print("We don't have it ")