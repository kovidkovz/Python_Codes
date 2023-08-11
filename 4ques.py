# Check if the first and last number of a list is the same
# Write a function to return True if the first and last number of a given list is same.
# If numbers are different then return False.
list=[1,2,3,4,5,6,1]
if list[0]==list[len(list)-1]:
    print(True)
else:
    print(False)