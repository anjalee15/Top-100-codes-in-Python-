# Sum of digits of a number
num=int(input("Enter a number : "))
sum=0
x=1
while x>0:
    x=num%10
    sum+=x
    num=num//10
print(sum)