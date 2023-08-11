# remove duplicates from a list
list=[1,2,4,3,2,6,7,1,4,5]
list1= []
for i in list:
    if list.count(i)<2:
        list1.append(i)
print(list1)