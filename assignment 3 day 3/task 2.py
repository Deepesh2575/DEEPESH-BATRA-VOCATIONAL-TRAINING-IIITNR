# Simple employee record example
employees = {
	101: {"Name": "Deepesh Batra", "Department": "IT", "Salary": 50000},
	102: {"Name": "Asha Rao", "Department": "HR", "Salary": 42000},
}

def display_emp(emp_id):
	e = employees.get(emp_id)
	if not e:
		print(f"No employee with ID {emp_id}")
		return
	print(f"ID: {emp_id}")
	for k, v in e.items():
		print(f"  {k}: {v}")

def update_salary(emp_id, new_salary):
	if emp_id in employees:
		employees[emp_id]["Salary"] = new_salary
		print(f"Updated salary for {emp_id} to {new_salary}")
	else:
		print(f"Employee {emp_id} not found")

def display_all():
	print("All employee keys and values:")
	for emp_id, info in employees.items():
		print(emp_id, info)

if __name__ == '__main__':
	display_emp(101)
	update_salary(101, 55000)
	display_emp(101)
	display_all()
