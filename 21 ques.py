# create a python program to find the factorial of a number in a single line
a=int(input("Number: "))
product=1
while a>0:
    product=product*a
    a=a-1
print(product)