def get_grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 75:
        return 'B'
    elif avg >= 50:
        return 'C'
    else:
        return 'Fail'

# Input student name
name = input("Enter student name: ")

# Input marks for 5 subjects
subjects = ['Math', 'English', 'Science', 'History', 'PE']
marks = {}

for subject in subjects:
    marks[subject] = float(input(f"Enter {subject} marks: "))

# Calculate total and average
total = sum(marks.values())
average = total / len(marks)
grade = get_grade(average)

# Display results
print("\n" + "="*40)
print(f"Student: {name}")
print("="*40)
for subject, mark in marks.items():
    print(f"{subject}: {mark}")
print("-"*40)
print(f"Total Marks: {total}")
print(f"Average Marks: {average:.2f}")
print(f"Grade: {grade}")
print("="*40)
