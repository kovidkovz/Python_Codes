# Group list elements based on frequency
list= [1, 3, 4, 4, 1, 5, 3, 1]
# Output : [(1, 3), (3, 2), (4, 2), (5, 1)]
# Python3 program to Grouping list
# elements based on frequency
lis=[]

for i in list:
    lis.append((i,list.count(i)))
print(lis)


