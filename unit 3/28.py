#  Sorting the dictionary elements using lambda (by using sorted () method)
# according to age and if age is same then sort my name
# Eg. stud= [{'name': 'Amit', 'age': 25}, {'name': 'Bina', 'age': 22}, {'name':
# 'Dax', 'age': 25}]

stud= [{'name': 'Amit', 'age': 25}, {'name': 'Bina', 'age': 22}, {'name': 'Dax', 'age': 25}]

ans  = sorted(stud,key=lambda x :x['age'],reverse=False)

print(ans)