# Remove first n characters from a string
# Write a program to remove characters from a string starting from zero up to n and return a new string.

n=int(input("Enter the len of characters you want to slice from the string: "))
str="kovid"
print(str[n:len(str)])


# # Alternate 
# def remove_chars(word, n):
#     print('Original string:', word)
#     x = word[n:]
#     return x

# print("Removing characters from a string")
# print(remove_chars("pynative", 4))
# print(remove_chars("pynative", 2))
