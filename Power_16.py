# Power of a number
b, p=map(int,input("Enter base and power separated by space ").split())
ans=1
for i in range(p):
    ans*=b
print(f"{b} to the power {p} is {ans}")