a=int(input("enter 1 number:"))
b=int(input("enter 2 number:"))
c=int(input("enter 3 number:"))
total=a+b+c
average=total/3
print("sum and average:",total,average)

if b>a and b>c:
    print("the largest is :",b)
elif c>a and c>b:
    print("the largest is :",c)
else:
    print("the largest is",a)

d=(a>0) and (b>0) and (c>0)
print("all the numbe are positive number?\n",d)