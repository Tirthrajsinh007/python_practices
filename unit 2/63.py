'''
Create a dictionary of employees where empId will be the key and value will
be the name of an employee
1. Display how many employees are there in the dictionary.
2. Display all empID and add them in a separate list.
3. Display all employee names and take them to a separate list
4. Take an empId from the user and check if that employee is
there in the dictionary or not.
5. If an empID is there in the dictionary then display the name of
that employee or if not available then add an ID and Name of
the employee in the dictionary
6. Change the name of the employee of empID taken by the user
7. Remove an employee whose ID is provided by the user

'''

emp = {
    101:"tirth",
    102:"gautam",
    103:"jaynit",
    104:"nitin",
    104:"jeel",
    106:"dhruv",
    107:"ankit",
    108:"nikunj"
}


print(emp)

print(len(emp))

print(list(emp.values()))

# inp = int(input("Enter Employee id for search"))

# if inp in emp:
#     print(f"{emp[inp]} is available in dictionary")
# else:
#     print("employee is not available so you need to add this employee. ")
#     emp_name = input("Enter Employee Name  :")
#     emp[inp] = emp_name
#     print("employee added successfully. ")

# print(emp)

# empid = int(input("Enter emp id : "))
# if empid in emp:
#     emp_name = input("Enter employee Name :")
#     emp[empid] = emp_name
# else:
#     print("employee id is not here ")

# print(emp)

empid = int(input("Enter emp id : "))

if empid in emp:
   emp.pop(empid)
print(emp)




