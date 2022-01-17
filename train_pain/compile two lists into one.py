list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
list3 = []
for i in list1:
    if i % 2:
        list3.append(i)
for i in list2:
    if not i % 2:
        list3.append(i)
print(list3)
