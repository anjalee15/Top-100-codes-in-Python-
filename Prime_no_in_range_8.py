# Prime numbers within a given range
n1=int(input("Enter the first number :"))
n2=int(input("Enter the second number :"))
p=[]
a=n2//2
for i in range(n1,n2):
    for j in range(2,a+1):
        if i%j==0:
            break
    else:
        p.append(i)
print("The prime numbers in the range {n1} to {n2} are :")
for i in p:
    print(i)