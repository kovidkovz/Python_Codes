# Remove all occurrences of a specific item from a list.
# Given a Python list, write a program to remove all occurrences of item 20.
list1 = [5, 20, 15, 20, 25, 50, 20]
# for i in range(len(list1)):
#     if list1[i]==20:
#         list1.pop(i)
# print(list1)

while 20 in list1:
    list1.remove(20)
print(list1)