a=[]
for i in range(5):
    b=float(input(f"enter the {i+1} number"))
    a.append(b)
c=sum(a)/len(a)
print("the average is :",c)