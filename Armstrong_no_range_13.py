# Armstrong number in a given range
n1, n2 =map(int, input("Enter inner and ourt range separated by space : ").split())
list1=[" "]
for i in range(n1,n2):
    nc=str(i)
    l=len(nc)
    n=i
    x=1
    s=0
    while(x>0):
        x=n%10
        s+=x**l
        n=n//10
    if s==i:
        list1.append(i)
print(f"Armstrong numbers in the range {n1} and {n2} are:")
for i in list1:
    print(i)