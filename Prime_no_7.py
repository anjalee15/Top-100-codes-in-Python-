# Prime number
n=int(input("Enter a number :"))
p=0
a=n//2
for i in range(2,a+1):
    if n%i==0:
        p=1
        break
if p==0:
    print(f"{n} is prime")
else:
    print(f"{n} is not prime")       