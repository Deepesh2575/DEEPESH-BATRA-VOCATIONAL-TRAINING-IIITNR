a=[]
for i in range(5):
    b=input(f"the {i+1} element is :")
    a.append(b)
for i in a:
    print(i)

#question 8
c=input("enter te fruit name of what you wnat to add but in last:")
a.append(c)
print(a)

#question 9
d=int(input("enter position to ennter:"))
e=input("enter the name of fruits:")
a.insert(d,e)
print(a)

#question 10
a.remove("zxc")
print(a)

#question 11
a.pop()
print(a)