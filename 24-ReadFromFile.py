with open("nameslist.txt", "r") as f:
    names = f.readlines()
    list_names = []
    count_names = {}
    for i in names:
        list_names.append(i.rstrip())
    for name in list_names:
        count_names[name] = list_names.count(name)
    print(count_names)
    print(list_names)
print()
with open("Training_01.txt", "r") as e:
    tra = e.readlines()
    new_dict = {}
    new_list = []
    for i in tra:
        new_list.append(i.rstrip().replace('/a/','').split('/'))
    lst1 = []
    for j in new_list:
        lst1.append(j[0])
    for theme in lst1:
        new_dict[theme] = lst1.count(theme)
    print(new_dict)