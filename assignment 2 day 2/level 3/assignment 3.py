list=["c","c++","java","python","javascript"]
print("the list of programming languages is:",list)
a=input("enter the programming language you want to add:")
list.append(a)
b=input("enter the programming language you want to remove:")
list.remove(b)
c=sorted(list)
print("the sorted list of programming languages is:",c)
print("the final list of programming languages is:",list)