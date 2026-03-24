students= {"amit","neha","riya","karan"}

if "riya" in students:
    print("yes")

math_student ={"amit","neha","riya"}
cs_student  = {"riya","karan","pooja"}
print(math_student & cs_student )

club_A = {"Rahul", "Sneha", "Amit"}
club_B = {"Sneha", "Karan", "Pooja"}
print(club_A ^ club_B)

course_A = {"Amit", "Neha", "Riya", "Karan"}
course_B = {"Neha", "Karan"}
print(course_A-course_B)

workshop1 = {"Amit", "Riya", "Pooja"}
workshop2 = {"Riya", "Karan", "Neha"}
print(workshop1-workshop2)

attendance = {"Amit", "Neha", "Riya", "Karan"}
attendance.remove("Neha")
print(attendance)

present_students = {"Ravi", "Sneha", "Amit"}
for i in present_students:
    print(i)

emails = ["a@gmail.com", "b@gmail.com", "a@gmail.com",
"c@gmail.com"]
print(set(emails))

class_A = {"Amit", "Neha"}
class_B = {"Amit", "Neha", "Riya", "Karan"}
flag =True
for i in class_A:
    if i not in class_B:
        flag =False
        break;
if flag:
    print("class a is subset of class b")
else:
    print("class a is not subset of class b")


team1 = {"Amit", "Riya"}
team2 = {"Karan", "Neha"}
if team1 & team2 == set():
    print("disjoin")
else:
    print("not disjoin")




