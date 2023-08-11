# to find a missing number in an arraay
array=[7,8,9,11,12,13]
list=[]
for i in range(len(array)-1):
    if array[i+1]!=array[i]+1:
        list.append(array[i]+1)
for ele in list:
    print(ele)
    
        
    