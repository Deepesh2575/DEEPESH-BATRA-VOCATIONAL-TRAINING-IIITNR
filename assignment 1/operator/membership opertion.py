list_programming=["c","c++","python","rust","ruby"]
a=input("enter a language:")
if a in list_programming:
    print("yes")
else:
    print("No")

b=12
c=10
d=[10]

print("the a in c",a is c)
print("the a is not c",(a is not c))
print("the b in c",b is c)
print("the b is not c",(b is not c))