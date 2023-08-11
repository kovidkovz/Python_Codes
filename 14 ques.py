# Find index of maximum item in list

list=[  2, 4, 6, 1, 8, 5, 3 ]
# Output:  Index of the max element in a list is 4
# Explanation: The max element is 8 and its position is 4.
for i in range(len(list)):
    if list[i]==max(list):
        print(i)
