# Leap Year
a=int(input("Enter a year : "))
if a%4==0:
    if a%100==0 :
        if a%400==0:
            print(f"{a} is a leap year")
    else:
        print(f"{a} is a leap year")
else:
    print(f"{a} is not a leap year")