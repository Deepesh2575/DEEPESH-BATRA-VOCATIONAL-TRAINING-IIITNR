student="deepesh"
roll_number=300012824017
branch="data Science"
marks=[]
for i in range(5):
    mark=float(input(f"the marks of {i+1} subject:"))
    marks.append(mark)

total=sum(marks)
average=total/5
percentage = (total/500)*100

print("name:",student)
print("roll number",roll_number)
print("branch",branch)
print("total obtin:",total)
print("average marks:",average)
print("perentage:",percentage)
