input=int(input("Enter a number: "))
array=[3,6,2,9,5]
list2=[]
for i in range(len(array)):
    for j in range(i):
        if array[i]+array[j]==input:
            list2.append((array[i],array[j]))
print(list2)

