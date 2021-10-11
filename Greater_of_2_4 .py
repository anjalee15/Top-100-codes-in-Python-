# Greater of 2 no
a, b= map(int,input().split())
if a>b:
    print(f"{a} is greater than {b}")
if a<b:
    print(f"{b} is greater than {a}")
else:
    print(f"{a} is equal to {b}")