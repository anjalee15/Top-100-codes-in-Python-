# Changing Case of a string -> Hello123 gives hELLO123
str1=input("Enter the string : ")
str2=""
for i in str1:
    if i.isalpha():
        if i.isupper():
            str2+=i.casefold()
        else:
            str2+=i.upper()
    else:
        str2+=i
print(str2)