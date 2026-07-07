def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y


def mod_inverse(a, m):
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        return None
    return x % m

def encrypt(p,k):
    result=""
    for i in range(len(p)):
        char = p[i]
        if char.isupper():
            result += chr(((ord(char) - ord('A')) * k) % 26 + ord('A'))
        elif char.islower():
            result += chr(((ord(char) - ord('A')) * k) % 26 + ord('A'))
        else:
            result += char
    return result
def decryt(c,k):
    f= mod_inverse(k, 26)

    if f is None:
        return "Invalid key! No modular inverse exists."

    result=""
    for i in range(len(c)):
        char = c[i]
        if char.isupper():
            result += chr(((ord(char) - ord('A')) * f) % 26 + ord('A'))
        elif char.islower():
            result += chr(((ord(char) - ord('A')) * f) % 26 + ord('A'))
        else:
            result += char
    return result
a=input("enter the plain text : ")
b=int(input("enter the security key:"))
c=encrypt(a,b)
print("the encrypt is :",c)
d=decryt(c,b)
print("the decrypt:",d)