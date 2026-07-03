def average(a,s,d,f,g):
    return (a+s+d+f+g)/5
a=[]
for i in range(5):
    a.append(float(input(f"enter the {i+1} number:")))
result=average(a[0],a[1],a[2],a[3],a[4])
print("the average of the five numbers is",result)