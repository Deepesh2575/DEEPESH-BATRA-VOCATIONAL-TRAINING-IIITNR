a=input("enter yout name:")
b=int(input("enter your roll number:"))
marks=[]
for i in range(5):
    c=float(input(f"enter marks of subject {i+1}:"))
    marks.append(c)
d=sum(marks)
e=len(marks)
f=d/e
g=(d/500)*100
print(f"total marks obtained by {a} is {d}")
print(f"average marks obtained by {a} is {f}")
print(f"percentage obtained by {a} is {g}")