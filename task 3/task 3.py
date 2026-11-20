
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# PART 1: NUMPY

marks = np.array([
    [85, 90, 80],
    [75, 80, 85],
    [90, 95, 88],
    [60, 70, 75]
])

print("NUMPY OPERATIONS")

print("Marks:")
print(marks)

print("Shape:", marks.shape)

student_avg = np.mean(marks, axis=1)
print("Student Averages:", student_avg)

subject_avg = np.mean(marks, axis=0)
print("Subject Averages:", subject_avg)

grace_marks = marks + 5
print("Grace Marks:")
print(grace_marks)

weights = np.array([0.4, 0.35, 0.25])
weighted_scores = np.dot(grace_marks, weights)

print("Weighted Scores:", weighted_scores)


# PART 2: CREATE EMPLOYEES CSV

employees = pd.DataFrame({
    'emp_id': [101, 102, 103, 104, 105, 106, 107, 108, 108],
    'name': [
        'Arun', 'Bala', 'Chitra', 'Divya',
        'Ezhil', 'Farhan', 'Gita', 'Hari', 'Hari'
    ],
    'department': [
        'Sales', 'Sales', 'HR', 'HR',
        'IT', 'IT', 'IT', 'Finance', 'Finance'
    ],
    'salary': [
        30000, 35000, 28000, np.nan,
        45000, np.nan, 50000, 40000, 40000
    ],
    'age': [25, 28, 26, 30, 32, 29, 35, 31, 31]
})

employees.to_csv("employees.csv", index=False)


# PART 3: CREATE DEPARTMENTS CSV

departments = pd.DataFrame({
    'department': [
        'Sales', 'HR', 'IT', 'Finance', 'Marketing'
    ],
    'head': [
        'Mr. Kumar', 'Mrs. Priya', 'Mr. Raj',
        'Ms. Lakshmi', 'Mr. Anand'
    ],
    'budget': [500000, 300000, 800000, 400000, 350000]
})

departments.to_csv("departments.csv", index=False)


# PART 4: LOAD AND EXPLORE DATA

df = pd.read_csv("employees.csv")

print("\nPANDAS OPERATIONS")

print(df)

print("\nDATA INFORMATION")
df.info()

print("\nSTATISTICS")
print(df.describe())

print("\nLOC")
print(df.loc[0:3, ['name', 'salary']])

print("\nILOC")
print(df.iloc[0:4, 0:3])

print("\nFILTERING")
print(df[df['salary'] > 30000])


# PART 5: DATA CLEANING

print("\nDATA CLEANING")

print("Missing values:")
print(df.isnull().sum())

# Fill missing salaries with median
df['salary'] = df['salary'].fillna(df['salary'].median())

# Remove duplicate rows
df = df.drop_duplicates()

# Correct data types
df['emp_id'] = df['emp_id'].astype(int)
df['salary'] = df['salary'].astype(float)
df['age'] = df['age'].astype(int)

print("\nCleaned Data:")
print(df)


# PART 6: GROUPBY

print("\nGROUPBY")

summary = df.groupby('department').agg(
    headcount=('emp_id', 'count'),
    average_salary=('salary', 'mean'),
    maximum_salary=('salary', 'max')
)

print(summary)


# PART 7: MERGING

departments = pd.read_csv("departments.csv")

print("\nINNER JOIN")
print(pd.merge(df, departments, on='department', how='inner'))

print("\nLEFT JOIN")
print(pd.merge(df, departments, on='department', how='left'))

print("\nOUTER JOIN")
print(pd.merge(df, departments, on='department', how='outer'))

# Find department without employees
no_employees = set(departments['department']) - set(df['department'])

print("\nDepartment without employees:")
print(no_employees)


# PART 8: MATPLOTLIB CHARTS

# BAR CHART
plt.figure()
plt.bar(summary.index, summary['average_salary'],
        color='skyblue', label='Average Salary')
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.legend()
plt.tight_layout()
plt.savefig("bar_chart.png")
plt.show()

# HISTOGRAM
plt.figure()
plt.hist(df['salary'], bins=5, color='orange',
         edgecolor='black', label='Salary')
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.legend()
plt.tight_layout()
plt.savefig("histogram.png")
plt.show()

# SCATTER PLOT
plt.figure()
plt.scatter(df['age'], df['salary'],
            color='green', label='Employees')
plt.title("Age vs Salary")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.legend()
plt.tight_layout()
plt.savefig("scatter_plot.png")
plt.show()

# LINE CHART
plt.figure()
plt.plot(df['emp_id'], df['salary'],
         marker='o', color='red', label='Salary')
plt.title("Employee Salary Trend")
plt.xlabel("Employee ID")
plt.ylabel("Salary")
plt.legend()
plt.tight_layout()
plt.savefig("line_chart.png")
plt.show()

print("\nAll charts saved successfully!")
