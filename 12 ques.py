#  Program to print duplicates from a list of integers
lis = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
uniqueList = []
duplicateList = []
 
for i in lis:
    if i not in uniqueList:
        uniqueList.append(i)
    elif i not in duplicateList:
        duplicateList.append(i)
 
print(duplicateList)