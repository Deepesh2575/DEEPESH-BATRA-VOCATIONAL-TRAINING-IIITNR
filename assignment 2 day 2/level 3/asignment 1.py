name,roll,marks=input("enter the name:roll:marks:").split()
roll=int(roll)
marks=int(marks)
print("Name:", name)
print("Roll:", roll)
print("Marks:", marks)
if float(marks) >= 50 and float(marks) <= 100:
    print("Result: Pass")
elif float(marks)>100:
    print("Marks should be less than or equal to 100")
else:
    print("Result: Fail")