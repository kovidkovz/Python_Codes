#  List product excluding duplicates
list=[1, 3, 5, 6, 3, 5, 6, 1]
list2=[]
for i in list:
    if i not in list2:
        list2.append(i)
print(list2)