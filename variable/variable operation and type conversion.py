
a=int(input("enter 1 number:"))
b=int(input("enter 2 number:"))
a,b=b,a
print("after swap : 1:",a,"2:",b)

n_int=1
n_float=9.02345
n_char="1234"

print("convert int to float:",float(n_int),"type:",type(float(n_int)))
print("convert float to int:",int(n_float),"type:",type(int(n_float)))
print("convert string to int:",int(n_char),"type:",type(int(n_char)))