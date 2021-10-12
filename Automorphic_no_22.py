num=int(input("Enter a number :"))
sq=num**2
if (num%10)==(sq%10):
    print(f"{num} is an automorphic number")
else:
    print(f"{num} is not an automorphic number")