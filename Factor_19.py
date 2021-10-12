#Finds factor of a number
n=int(input("Enter a number : "))
fact=[]
for i in range(1,n):
    if n%i==0:
        fact.append(i)
print(f"The Factors of {n} are :")
for i in fact:
    print(i,end=" ")