# the given number is a palindrome or not
num=input("Enter a number: ")
rev=num[::-1]
if num==rev:
    print(f"{num} is a palindrome")
else:
    print(f"{num} is not a palindrome")