# Iterate both lists simultaneously
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
list=list2[::-1]
for x, y in zip(list1 , list):
    print(x,y)
    