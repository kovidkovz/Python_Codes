# Difference between two lists


# Input:
list1 = [10, 15, 20, 25, 30, 35, 40]
list2 = [25, 40, 35] 

# Output:
# [10, 20, 30, 15]
list=[]
for i in list1:
    if i not in list2:
        list.append(i)
print(list)

