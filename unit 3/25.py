# 25 Add all the elements of the list (using reduce())
from functools import reduce;


ans = reduce(lambda x,y: x+y,[x for x in range(10)])

print(ans)