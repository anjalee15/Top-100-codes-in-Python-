num=int(input("Enter a number : "))
lst=[]
for i in range(1,num):
    if num%i==0:
        lst.append(i)
if num==sum(lst):
    print(f"{num} is a perfect number")
else:
    print(f"{num} is not a perfect number")
