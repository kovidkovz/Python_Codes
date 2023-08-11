# /Python – Extract elements with Frequency greater than K
# Input : test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8], K = 3 
# Output : [4, 3] 
# Explanation : Both elements occur 4 times. 
test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
list=[]
for i in test_list:
    if test_list.count(i)>3 and i not in list:
        list.append(i)
print(list)
