# Python program to find smallest number in a list
list1 = [10, 20, 4]
print(min(list1))

list1.sort()
print(list1[0])

list1.sort(reverse=True)
print(list1[len(list1)-1])