#  Print the sum of the current number and the previous number
previous_num=0
for i in range (1,11):
    sum=previous_num+i
    print("the previous number is",previous_num,"the current number is",i,"sum:",sum)
    previous_num=i