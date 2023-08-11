# Python program to find the Strongest Neighbour
# Input: 1 2 2 3 4 5
# Output: 2 2 3 4 5
list=[4,1,2,3,6,2,5]
list1=[]
for i in range(len(list)-1):
    if list[i]>list[i+1]:
        list1.append(list[i])
    else:
        list1.append(list[i+1])
print(list1)