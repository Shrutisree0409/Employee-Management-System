#!/usr/bin/env python
# coding: utf-8

# # ***Employee Management System (EMS)***
# 
# ### Objective - Create a simplified Employee Management System (EMS). This project will cover control structures, functions, and object-oriented programming concepts to manage employee data.
# 

# In[10]:


employees = {
    101: {'name': 'Employee1', 'age': 22, 'department': 'HR', 'salary': 30000},
    102: {'name': 'Employee2', 'age': 23, 'department': 'Finance', 'salary': 31000},
    103: {'name': 'Employee3', 'age': 24, 'department': 'IT', 'salary': 32000},
    104: {'name': 'Employee4', 'age': 25, 'department': 'Marketing', 'salary': 33000},
    105: {'name': 'Employee5', 'age': 26, 'department': 'Sales', 'salary': 34000},
    106: {'name': 'Employee6', 'age': 27, 'department': 'HR', 'salary': 35000},
    107: {'name': 'Employee7', 'age': 28, 'department': 'Finance', 'salary': 36000},
    108: {'name': 'Employee8', 'age': 29, 'department': 'IT', 'salary': 37000},
    109: {'name': 'Employee9', 'age': 30, 'department': 'Marketing', 'salary': 38000},
    110: {'name': 'Employee10', 'age': 31, 'department': 'Sales', 'salary': 39000},
    111: {'name': 'Employee11', 'age': 22, 'department': 'HR', 'salary': 40000},
    112: {'name': 'Employee12', 'age': 23, 'department': 'Finance', 'salary': 41000},
    113: {'name': 'Employee13', 'age': 24, 'department': 'IT', 'salary': 42000},
    114: {'name': 'Employee14', 'age': 25, 'department': 'Marketing', 'salary': 43000},
    115: {'name': 'Employee15', 'age': 26, 'department': 'Sales', 'salary': 44000},
    116: {'name': 'Employee16', 'age': 27, 'department': 'HR', 'salary': 45000},
    117: {'name': 'Employee17', 'age': 28, 'department': 'Finance', 'salary': 46000},
    118: {'name': 'Employee18', 'age': 29, 'department': 'IT', 'salary': 47000},
    119: {'name': 'Employee19', 'age': 30, 'department': 'Marketing', 'salary': 48000},
    120: {'name': 'Employee20', 'age': 31, 'department': 'Sales', 'salary': 49000},
    121: {'name': 'Employee21', 'age': 22, 'department': 'HR', 'salary': 50000},
    122: {'name': 'Employee22', 'age': 23, 'department': 'Finance', 'salary': 51000},
    123: {'name': 'Employee23', 'age': 24, 'department': 'IT', 'salary': 52000},
    124: {'name': 'Employee24', 'age': 25, 'department': 'Marketing', 'salary': 53000},
    125: {'name': 'Employee25', 'age': 26, 'department': 'Sales', 'salary': 54000},
    126: {'name': 'Employee26', 'age': 27, 'department': 'HR', 'salary': 55000},
    127: {'name': 'Employee27', 'age': 28, 'department': 'Finance', 'salary': 56000},
    128: {'name': 'Employee28', 'age': 29, 'department': 'IT', 'salary': 57000},
    129: {'name': 'Employee29', 'age': 30, 'department': 'Marketing', 'salary': 58000},
    130: {'name': 'Employee30', 'age': 31, 'department': 'Sales', 'salary': 59000},
    131: {'name': 'Employee31', 'age': 22, 'department': 'HR', 'salary': 60000},
    132: {'name': 'Employee32', 'age': 23, 'department': 'Finance', 'salary': 61000},
    133: {'name': 'Employee33', 'age': 24, 'department': 'IT', 'salary': 62000},
    134: {'name': 'Employee34', 'age': 25, 'department': 'Marketing', 'salary': 63000},
    135: {'name': 'Employee35', 'age': 26, 'department': 'Sales', 'salary': 64000},
    136: {'name': 'Employee36', 'age': 27, 'department': 'HR', 'salary': 65000},
    137: {'name': 'Employee37', 'age': 28, 'department': 'Finance', 'salary': 66000},
    138: {'name': 'Employee38', 'age': 29, 'department': 'IT', 'salary': 67000},
    139: {'name': 'Employee39', 'age': 30, 'department': 'Marketing', 'salary': 68000},
    140: {'name': 'Employee40', 'age': 31, 'department': 'Sales', 'salary': 69000},
    141: {'name': 'Employee41', 'age': 22, 'department': 'HR', 'salary': 70000},
    142: {'name': 'Employee42', 'age': 23, 'department': 'Finance', 'salary': 71000},
    143: {'name': 'Employee43', 'age': 24, 'department': 'IT', 'salary': 72000},
    144: {'name': 'Employee44', 'age': 25, 'department': 'Marketing', 'salary': 73000},
    145: {'name': 'Employee45', 'age': 26, 'department': 'Sales', 'salary': 74000},
    146: {'name': 'Employee46', 'age': 27, 'department': 'HR', 'salary': 75000},
    147: {'name': 'Employee47', 'age': 28, 'department': 'Finance', 'salary': 76000},
    148: {'name': 'Employee48', 'age': 29, 'department': 'IT', 'salary': 77000},
    149: {'name': 'Employee49', 'age': 30, 'department': 'Marketing', 'salary': 78000},
    150: {'name': 'Employee50', 'age': 31, 'department': 'Sales', 'salary': 79000},
    151: {'name': 'Employee51', 'age': 22, 'department': 'HR', 'salary': 80000},
    152: {'name': 'Employee52', 'age': 23, 'department': 'Finance', 'salary': 81000},
    153: {'name': 'Employee53', 'age': 24, 'department': 'IT', 'salary': 82000},
    154: {'name': 'Employee54', 'age': 25, 'department': 'Marketing', 'salary': 83000},
    155: {'name': 'Employee55', 'age': 26, 'department': 'Sales', 'salary': 84000},
    156: {'name': 'Employee56', 'age': 27, 'department': 'HR', 'salary': 85000},
    157: {'name': 'Employee57', 'age': 28, 'department': 'Finance', 'salary': 86000},
    158: {'name': 'Employee58', 'age': 29, 'department': 'IT', 'salary': 87000},
    159: {'name': 'Employee59', 'age': 30, 'department': 'Marketing', 'salary': 88000},
    160: {'name': 'Employee60', 'age': 31, 'department': 'Sales', 'salary': 89000},
    161: {'name': 'Employee61', 'age': 22, 'department': 'HR', 'salary': 90000},
    162: {'name': 'Employee62', 'age': 23, 'department': 'Finance', 'salary': 91000},
    163: {'name': 'Employee63', 'age': 24, 'department': 'IT', 'salary': 92000},
    164: {'name': 'Employee64', 'age': 25, 'department': 'Marketing', 'salary': 93000},
    165: {'name': 'Employee65', 'age': 26, 'department': 'Sales', 'salary': 94000},
    166: {'name': 'Employee66', 'age': 27, 'department': 'HR', 'salary': 95000},
    167: {'name': 'Employee67', 'age': 28, 'department': 'Finance', 'salary': 96000},
    168: {'name': 'Employee68', 'age': 29, 'department': 'IT', 'salary': 97000},
    169: {'name': 'Employee69', 'age': 30, 'department': 'Marketing', 'salary': 98000},
    170: {'name': 'Employee70', 'age': 31, 'department': 'Sales', 'salary': 99000},
    171: {'name': 'Employee71', 'age': 22, 'department': 'HR', 'salary': 100000},
    172: {'name': 'Employee72', 'age': 23, 'department': 'Finance', 'salary': 101000},
    173: {'name': 'Employee73', 'age': 24, 'department': 'IT', 'salary': 102000},
    174: {'name': 'Employee74', 'age': 25, 'department': 'Marketing', 'salary': 103000},
    175: {'name': 'Employee75', 'age': 26, 'department': 'Sales', 'salary': 104000},
    176: {'name': 'Employee76', 'age': 27, 'department': 'HR', 'salary': 105000},
    177: {'name': 'Employee77', 'age': 28, 'department': 'Finance', 'salary': 106000},
    178: {'name': 'Employee78', 'age': 29, 'department': 'IT', 'salary': 107000},
    179: {'name': 'Employee79', 'age': 30, 'department': 'Marketing', 'salary': 108000},
    180: {'name': 'Employee80', 'age': 31, 'department': 'Sales', 'salary': 109000},
    181: {'name': 'Employee81', 'age': 22, 'department': 'HR', 'salary': 110000},
    182: {'name': 'Employee82', 'age': 23, 'department': 'Finance', 'salary': 111000},
    183: {'name': 'Employee83', 'age': 24, 'department': 'IT', 'salary': 112000},
    184: {'name': 'Employee84', 'age': 25, 'department': 'Marketing', 'salary': 113000},
    185: {'name': 'Employee85', 'age': 26, 'department': 'Sales', 'salary': 114000},
    186: {'name': 'Employee86', 'age': 27, 'department': 'HR', 'salary': 115000},
    187: {'name': 'Employee87', 'age': 28, 'department': 'Finance', 'salary': 116000},
    188: {'name': 'Employee88', 'age': 29, 'department': 'IT', 'salary': 117000},
    189: {'name': 'Employee89', 'age': 30, 'department': 'Marketing', 'salary': 118000},
    190: {'name': 'Employee90', 'age': 31, 'department': 'Sales', 'salary': 119000},
    191: {'name': 'Employee91', 'age': 22, 'department': 'HR', 'salary': 120000},
    192: {'name': 'Employee92', 'age': 23, 'department': 'Finance', 'salary': 121000},
    193: {'name': 'Employee93', 'age': 24, 'department': 'IT', 'salary': 122000},
    194: {'name': 'Employee94', 'age': 25, 'department': 'Marketing', 'salary': 123000},
    195: {'name': 'Employee95', 'age': 26, 'department': 'Sales', 'salary': 124000},
    196: {'name': 'Employee96', 'age': 27, 'department': 'HR', 'salary': 125000},
    197: {'name': 'Employee97', 'age': 28, 'department': 'Finance', 'salary': 126000},
    198: {'name': 'Employee98', 'age': 29, 'department': 'IT', 'salary': 127000},
    199: {'name': 'Employee99', 'age': 30, 'department': 'Marketing', 'salary': 128000},
    200: {'name': 'Employee100', 'age': 31, 'department': 'Sales', 'salary': 129000}
}


# In[11]:


def add_employee():

    emp_id = int(input("Enter Employee ID: "))

    while emp_id in employees:
        print("Employee ID already exists!")

        emp_id = int(
            input("Enter a new Employee ID: ")
        )

    name = input("Enter Employee Name: ")

    age = int(
        input("Enter Employee Age: ")
    )

    department = input(
        "Enter Department: "
    )

    salary = float(
        input("Enter Salary: ")
    )

    employees[emp_id] = {
        "name": name,
        "age": age,
        "department": department,
        "salary": salary
    }

    print("Employee added successfully!")


# In[12]:


def view_employees():

    if len(employees) == 0:
        print("No employees available.")
        return

    print("\nID\tName\tAge\tDepartment\tSalary")
    print("_" * 50)

    for emp_id, details in employees.items():

        print(
            f"{emp_id}\t"
            f"{details['name']}\t"
            f"{details['age']}\t"
            f"{details['department']}\t"
            f"{details['salary']}"
        )


# In[13]:


def search_employee():

    emp_id = int(
        input("Enter Employee ID to Search: ")
    )

    if emp_id in employees:

        emp = employees[emp_id]

        print("\nEmployee Found!!!!")
        print("Name:", emp["name"])
        print("Age:", emp["age"])
        print("Department:", emp["department"])
        print("Salary:", emp["salary"])

    else:
        print("Employee not found.")


# In[14]:


def main_menu():

    while True:

        print("\n===== Employee Management System =====")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search Employee")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_employee()

        elif choice == "2":
            view_employees()

        elif choice == "3":
            search_employee()

        elif choice == "4":
            print("Thank you for using EMS!")
            break

        else:
            print("Invalid choice. Please try again.")


# In[ ]:


main_menu()


# In[ ]:




