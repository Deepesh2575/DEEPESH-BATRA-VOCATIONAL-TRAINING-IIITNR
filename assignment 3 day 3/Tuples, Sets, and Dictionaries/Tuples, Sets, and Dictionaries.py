a=()
for i in range(1,6):
    c=input(f"enter the {i} name of fruits:")
    a+=(c,)
print(a)
print("the first fruit is",a[0])
print("the last fruit is",a[-1])

b=set()
for i in range(1,6):
    c= input(f"enter the {i} name of fruits for set:")
    b.add(c)
print(b)
d=input("enter the name of fruits you want to add:")
b.add(d)
print(b)

e=input("enter the name of fruits you want to remove:")
b.remove(e)

f={}#dictionary
for i in range(1,3):
    g=input(f"enter the name of {i} person:")
    h=int(input(f"enter the age of {i} person:"))
    j=input(f"enter the city of {i} person:")
    #making a dictionary of dictionaries
    f[g]={"name":g,"age":h,"city":j}
print(f)
#display the name only
for i in f:
    print(f[i]["name"])

# add the new key "course" to each person's dictionary
for i in f:
    f[i]["course"] = input(f"enter the course of {f[i]['name']}:")

print(f)