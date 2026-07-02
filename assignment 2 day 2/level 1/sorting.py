a=[]
for i in range(5):
    b=float(input(f"enter the {i+1} number:"))
    a.append(b)
a.sort()
print("the ascending order:",a)
a.sort(reverse=True)
print("the desending order:",a)

print("the maximam number is :",max(a))
print("the minimum number is :",min(a))
print("the sum of list is:",sum(a))