# Python program to count Even and Odd numbers in a List
list1 = [2, 7, 5, 64, 14,3,6,1,17]
count_even=0
count_odd=0
for i in list1:
    if i%2==0:
        count_even+=1
    else:
        count_odd+=1
print("Count of even numbers:",count_even)
print("count of odd numbers:",count_odd)