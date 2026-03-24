# 25 Add all the elements of the list (using reduce())

from functools import reduce;
lst = [1,2,3,4,5]

ans = reduce(lambda x,y: x*y,lst)

print(ans)