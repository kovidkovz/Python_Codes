# Count occurrences of an element in a list
lst = [15, 6, 7, 10, 12, 20, 10, 28, 10]
count=0
for i in range(len(lst)):
    if lst[i]==10:
        count+=1
print(count)
