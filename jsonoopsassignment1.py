import json

class Employee:
    def __init__(self, name, dob, height, city, state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state

    def __str__(self):
        return f"Name: {self.name}, DOB: {self.dob}, Height: {self.height}, City: {self.city}, State: {self.state}"

# Function to read employee information from JSON file
def read_employee_info_from_json(empdet):
    with open(empdet, 'r') as file:
        data = json.load(file)
        employees = []
        for emp_data in data['employees']:
            employee = Employee(emp_data['Name'], emp_data['DOB'], emp_data['Height'], emp_data['City'], emp_data['State'])
            employees.append(employee)
        return employees

# Creating employee.json file
employee_data = {
    'employees': [
        {"Name": "Mukul", "DOB": "1993-06-26", "Height": 175, "City": "Jhalda", "State": "WB"},
        {"Name": "nitesh", "DOB": "1995-05-22", "Height": 162, "City": "Ranchi", "State": "JH"},
        {"Name": "Manish", "DOB": "1993-05-12", "Height": 181, "City": "Patna", "State": "BR"},
        {"Name": "Bikram", "DOB": "1992-03-29", "Height": 169, "City": "Cuttak", "State": "OR"},
        {"Name": "Akash", "DOB": "1995-09-07", "Height": 179, "City": "Pune", "State": "MH"}
    ]
}

with open('employee.json', 'w') as file:
    json.dump(employee_data, file, indent=2)

# Read employee information from JSON file and create Employee objects
employees_list = read_employee_info_from_json('employee.json')

# Print the list of Employee objects
for emp in employees_list:
    print(emp)
