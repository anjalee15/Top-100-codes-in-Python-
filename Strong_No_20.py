num= int(input("Enter a number : "))
n=num
x=1
s=0
while(n!=0):
    x=n%10
    n=n//10
    f=1
    for i in range(1,x+1):
        f*=i   
    s+=f

if num==s:
    print(f"{num} is a strong number")
else:
    print(f"{num} is not a strong number")



