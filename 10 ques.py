# Python program to print all odd numbers in a range
start=4
end=15
list=[]
for i in range(start,end+1):
    if i%2!=0:
        list.append(i)
print(list)