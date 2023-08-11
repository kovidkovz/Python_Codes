# Sum of number digits in List
list=[12, 67, 98, 34]
list1=[]
for num in list:
    sum=0
    for digit in str(num):
        sum+=int(digit)
    list1.append(sum)
print(list1) 