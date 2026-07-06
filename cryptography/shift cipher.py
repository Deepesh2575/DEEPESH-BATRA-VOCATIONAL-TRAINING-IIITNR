def encrypt(p,k):
    result=""
    for i in range(len(p)):
        char = p[i]
        if char.isupper():
            result += chr((ord(char) - ord('A') + k) % 26 + ord('A'))
        elif char.islower():
            result += chr((ord(char) - ord('a') + k) % 26 + ord('a'))
        else:
            result += char
    return result
def decryt(c,k):
    result=""
    for i in range(len(c)):
        char = c[i]
        if char.isupper():
                result += chr((ord(char) - ord('A') - k) % 26 + ord('A'))
        elif char.islower():
            result += chr((ord(char) - ord('a') - k) % 26 + ord('a'))
        else:
            result += char
    return result
a=input("enter the plain text : ")
b=int(input("enter the security key:"))
c=encrypt(a,b)
print("the encrypt is :",c)
d=decryt(c,b)
print("the decrypt",d)