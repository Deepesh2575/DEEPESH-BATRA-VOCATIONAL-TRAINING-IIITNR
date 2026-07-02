a=int(input("enter the 1 number:"))
b=int(input("enter the 2 number:"))
c=int(input("enter the 3 number:"))
if a>b and a>c:
    print(f"{a} is largest number.")
elif b>a and b>c:
    print(f"{b} is largest number.")
else:
    print(f"{c} is largest number.")