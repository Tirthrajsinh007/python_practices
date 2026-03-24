# Take a list of students and filter the students whose name is less than 6
# characters.

lst = ["tirth","nikunj","jeel"]

ans = list(filter(lambda x : x if len(x)<6 else 0,lst))
print(ans)