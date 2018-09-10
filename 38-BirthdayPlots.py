
from bokeh.plotting import figure, show, output_file
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

score=[1,2,3,4,5,6,7]
with open("birthdays.json", "r") as f:
    birthday = json.load(f)

months = []
for name, birthdates in birthday.items():
    month = int(birthdates.split("/")[1])
    months.append(num_to_string[month])
c = Counter(months)

output_file("plot.html")
x_categories = list(num_to_string.values())
x = list(c.keys())
y = list(c.values())

p = figure(x_range=x_categories)
p.vbar(x=x, top=y, width=0.5)


show(p)








