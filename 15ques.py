num=int(input("Enter a number:"))
reverse=0
while num>0:
    remainder=num%10
    reverse=reverse*10+remainder
    num=num//10
num2=int(input("re-enter the number"))
if num2==reverse:
    print("it is a palindrome")
else:
    print("it is not a palindrome")