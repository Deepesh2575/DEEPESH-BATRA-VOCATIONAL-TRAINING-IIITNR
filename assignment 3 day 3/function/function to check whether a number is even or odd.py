def even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
a=int(input("Enter a number: "))
result = even_odd(a)
print(f"The number {a} is {result}.")