# Use a lambda function to calculate grades for a list of scores (using map())
# Eg scores = [88, 92, 78, 95, 86]

scores = [88, 92, 78, 95, 86]
grades =[]

ans =  list(map(lambda x: grades.append("A") if x>=90 else (grades.append("B") if x>=80 and x<90 else grades.append("C")),[x for x in scores]))
print(grades)