# Check if previous element is smaller in List
test_list = [1, 3, 2, 6, 8]
list=[]
for i in  range(len(test_list)):
    for j in range(1,i+1):
        if test_list[i]<test_list[j]:
            list.append(False)
    else:
        list.append(True)
print(list)