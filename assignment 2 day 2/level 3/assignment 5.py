a = float(input("a: "))
b = float(input("b: "))
op = input("op: ")

if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
elif op == '*':
    print(a * b)
elif op == '/' and b != 0:
    print(a / b)
elif op == '/':
    print("Can't divide by zero")
else:
    print("Invalid operator")
