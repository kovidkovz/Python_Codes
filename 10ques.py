# Create a new list from a two list using the following condition

# Given a two list of numbers, write a program to create a new list such that
# the new list should contain odd numbers from the first list and even numbers from the second list.
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
list=[]
for i in list1:
    if i%2!=0:
        list.append(i)
for j in list2:
    if j%2==0:
        list.append(j)

print(list)