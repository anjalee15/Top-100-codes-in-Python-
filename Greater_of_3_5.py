#Greater of 3 nos
a,b,c= map(int,input("Enter 3 numbers separated by space : ").split())
if a>b and a>c:
    print(f"{a} is greater than {b} and {c}")
elif b>c and b>a:
    print(f"{b} is greater than {a} and {c}")
elif c>a and c>b:
    print(f"{c} is greater than {a} and {b}") 