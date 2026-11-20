
# 1. Function using *args and **kwargs
def bonus(salary, rate=0.1, *extras, **options):
    result = salary * rate + sum(extras)

    if 'cap' in options:
        result = min(result, options['cap'])

    return result


print("Bonus:", bonus(50000, 0.1, 500, 1000, cap=6000))


# 2. Custom Exception
class InvalidSalaryError(Exception):
    pass


# 3. Employee Class
class Employee:
    def __init__(self, name, salary):
        if salary < 0:
            raise InvalidSalaryError(f"Invalid salary: {salary}")

        self.name = name
        self.salary = salary

    def annual_salary(self):
        return self.salary * 12

    def get_details(self):
        return f"Name: {self.name}, Salary: {self.salary}"


# 4. Manager Class (Inheritance)
class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def get_details(self):
        return (super().get_details() +
                f", Team Size: {self.team_size}")


# Creating Employee and Manager objects
emp = Employee("Arun", 30000)
mgr = Manager("Rahul", 60000, 5)

print(emp.get_details())
print("Annual Salary:", emp.annual_salary())
print(mgr.get_details())


# 5. Handling Custom Exception
try:
    emp2 = Employee("Test", -500)

except InvalidSalaryError as e:
    print("Error:", e)

finally:
    print("Transaction finished")


# 6. Employee Data
employees = [
    {"id": 1, "name": "Arun", "department": "Sales",
     "salary": 30000, "city": "Chennai"},

    {"id": 2, "name": "Priya", "department": "HR",
     "salary": 45000, "city": "Chennai"},

    {"id": 3, "name": "Rahul", "department": "IT",
     "salary": 60000, "city": "Bangalore"},

    {"id": 4, "name": "Divya", "department": "IT",
     "salary": 75000, "city": "Chennai"},

    {"id": 5, "name": "Karthik", "department": "Finance",
     "salary": 90000, "city": "Mumbai"},

    {"id": 6, "name": "Meena", "department": "Sales",
     "salary": 52000, "city": "Bangalore"},

    {"id": 7, "name": "Suresh", "department": "IT",
     "salary": 68000, "city": "Chennai"},

    {"id": 8, "name": "Anitha", "department": "HR",
     "salary": 48000, "city": "Mumbai"}
]


# 7. List Comprehension
above_50000 = [
    emp["name"] for emp in employees
    if emp["salary"] > 50000
]

print("Above 50000:", above_50000)


# 8. Map and Lambda - Add 10% Raise
salaries = list(map(
    lambda emp: emp["salary"] * 1.10,
    employees
))

print("Salaries after 10% raise:", salaries)


# 9. Filter - Chennai Employees
chennai_employees = list(filter(
    lambda emp: emp["city"] == "Chennai",
    employees
))

print("Chennai:", [
    emp["name"] for emp in chennai_employees
])


# 10. For Loop with Continue and Break
print("Loop salaries:")

for emp in employees:
    salary = emp["salary"]

    if salary == 0:
        continue

    if salary > 85000:
        break

    print(emp["name"], salary)

