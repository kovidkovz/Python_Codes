#  Concatenate two lists in the following order
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
list=[]
for i in range(len(list1)):
    for j in range(i+1):
        list.append(list1[i]+list2[j])
print(list)

list=[x+y for x in list1 for  y in list2 ]
print(list)