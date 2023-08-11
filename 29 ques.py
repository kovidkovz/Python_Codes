list=[1,2,3,4,5,6]
count1=0
count2=0
for i in list:
    if i%2==0:
        count1+=1
    else:
        count2+=1
print("count of even",count1)
print("count of odd",count2)