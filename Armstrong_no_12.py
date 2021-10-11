# Given number is Armstrong number or not
num=input()
nc=int(num)
l=len(num)
n=nc
x=1
s=0
while(x>0):
    x=n%10
    s+=x**l
    n=n//10
if s==nc:
    print(f"{nc} is an Armstrong number")
else:
    print(f"{nc} is not an Armstrong number")