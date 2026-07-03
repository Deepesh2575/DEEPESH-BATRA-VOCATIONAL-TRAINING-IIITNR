a=int(input("enter the first number:"))
b=int(input("enter the last number:"))
count=0
for i in range(a,b+1):
    if i%2==0:
        count+=1
print("the number of even numbers between",a,"and",b,"is",count)