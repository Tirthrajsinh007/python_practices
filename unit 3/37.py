# 37 Create a menu driven program with user defined functions to insert update
# delete elements in the dictionary object of employees
# Emp = {empCode:[name, age, salary, (expert areas)],…..}


emp = {
    101:["tirth",21,100000,("python","java","ds")],
    102:["nikunj",22,80000,("js","java","sql")],
    103:["jaynit",32,700000,("python","java","C")],
    104:["jeel",22,50000,("react","node","c++")]
}

ch = int(input("Enter Your Choice :"))

def ins():
    emp_code = input("Enter code :")
    name = input("Enter Employee Name :")
    age = input("Enter Age : ")
    salary = input("Enter Salary :")
    experties = input("Enter Expertises :")
    emp[emp_code]:[name,age,salary,experties]

def upd():
    pass

def dele():
    pass
if(ch == 1):
    ins()
elif ch==2:
    upd()
elif ch ==3:
    dele()

