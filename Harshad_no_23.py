n=int(input("Enter a number : "))
num=n
x=0
s=0
while(num!=0):
    x=num%10
    s+=x
    num=num//10
if n%s==0:
    print(f"{n} is a Harshad number")
else:
    print(f"{n} is not a Harshad number")
