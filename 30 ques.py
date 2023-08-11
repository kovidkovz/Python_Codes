# Remove all the occurrences of an element from a list in Python
list=[1, 1, 2, 3, 4, 5, 1, 2] 
list2=[]
for i in list:
    if list.count(i)<2:
        list2.append(i)
print(list2)
