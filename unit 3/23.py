# Find the square of each element of a list (using map())
lst = [88,92,78,95,86]
ans  = list(map(lambda x:x*x ,[x for x in lst]))

print(ans)