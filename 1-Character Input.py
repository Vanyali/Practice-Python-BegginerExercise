import datetime
while True:
    try:
        name = input("What's your name?\n")
        age = int(input("Please enter your age: "))
        copies = int(input("Please enter the number of copies you want me to print in the terminal: "))
    except ValueError:
        print("Insert age/copies with integers, please!")
        continue
    else:
        break
    
actual_year = int(datetime.datetime.now().year)
birth_date = (actual_year - age)
year_100_age = birth_date + 100
years_left = year_100_age - actual_year

result = f"{name} you are going to be 100 years old in {year_100_age}, remaining years to reach it, {years_left}!"    
print("***ORIGINAL***")
print(result)
print()
print("Entering Extra Printing!\n")
count = 1
while count < (copies + 1):
    print(f"{count}:", result)
    count += 1
    




