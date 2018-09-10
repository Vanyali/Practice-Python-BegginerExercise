import json 
from collections import Counter


num_to_string = {
	1: "January",
	2: "February",
	3: "March", 
	4: "April",
	5: "May",
	6: "June",
	7: "July",
	8: "August",
	9: "September",
	10: "October",
	11: "November",
	12: "December"
}


'''
with open("birthdays.json", "r") as f:
    birthday = json.load(f)
month = []
for i, k in birthday.items():
    a = k.split("/")
    month_split = a[1]
    month.append(month_split)
print(Counter(month))
'''
with open("birthdays.json", "r") as f:
    birthday = json.load(f)

months = []
for name, birthdates in birthday.items():
    month = int(birthdates.split("/")[1])
    months.append(num_to_string[month])

print(months)

print(Counter(months))


