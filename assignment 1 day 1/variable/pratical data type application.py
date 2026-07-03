a=input("enter the product name :")
b=int(input("enter the price of that product:"))
c=0.18
d=int(input("rnter the quantity you wnat:"))
print("the suntotal price:",b*d)
print("the gst price",(b*d)*c)
print("the final price:",(b*d)+((b*d)*c))