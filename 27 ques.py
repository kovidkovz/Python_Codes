# Python program to check if the list contains three consecutive common numbers in Python

# Input : [4, 5, 5, 5, 3, 8]

# Output : 5

list=[4, 5, 5, 5, 3, 8,4,4]
list1=[]
for i in range(len(list)-2):
    if list[i]==list[i+1] and list[i+1]==list[i+2] and list[i] not in list1:
        list1.append(list[i])
print(list1)