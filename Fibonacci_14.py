# Fibonacci series upto n
n=int(input("Enter number of terms : "))
n1=0
n2=1
#10
print(f"{n1} {n2}",end=' ')
for i in range(n-2):
    x=n1
    n1=n2
    n2=x+n1
    print(n2,end=' ')

       


    