with open("happynumbers.txt", "r") as f:
    happy = f.readlines()
    happylist = []
    for i in happy:
        happylist.append(i.rstrip())
    print(happylist)
print()
with open("primenumbers.txt", "r") as e:
    prime = e.readlines()
    primelist = []
    for i in prime:
        primelist.append(i.rstrip())
    print(primelist)

print()
overlappinglist = []
for i in happylist:
    if i in primelist:
        overlappinglist.append(i)
print(overlappinglist)

