# students ={
#     "tirth":[21,"mca","python"],
#     "anknit":[22,"mba","marketing"],
#     "jaynit":[21,"ma","sociology"],
#     "nikunj":[24,"mca","js"],
#     "dhruv":[20,"mca","java"],
#     "jeel":[20,"bca","python"]
# }

# # student =[]

# min_age  = min(i[0] for i in students.values())

# print(min_age)
# print(students.values())
# t= students.values()

# for i in t:
#     if i[0] == min_age:
#         print(i)


 
marks = {}

for i in  range(2):
    rollno = int(input("Enter roll number :"))
    s1 = int(input("enter 1st Subject marks :"))    
    s2 = int(input("enter 2st Subject marks :"))    
    s3 = int(input("enter 3st Subject marks :"))    
    s4 = int(input("enter 4st Subject marks :"))    
    s5 = int(input("enter 5st Subject marks :"))    
    marks[rollno] = [s1,s2,s3,s4,s5];

print(marks)
        

new ={}


for i in marks:
    total=0
    for j in i:
        total = total +j;
        

print(total)
