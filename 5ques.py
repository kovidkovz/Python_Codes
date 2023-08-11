# write a program to enter even numbers into a list
# list=[]
# for i in range(11):
#     if i%2==0:
#         list.append(i)
# print("List of even numbers from 0 to 11:",list)

len=int(input("enter the length of a list: "))
list=[]
for i in range(len):
    Number=int(input("Enter a number to insert into a list: "))
    list.append(Number)
print(list)
