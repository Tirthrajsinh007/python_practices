from functools import reduce;
lst = [1,2,6,4,5]

ans = reduce(lambda x,y:x if x>y else y,lst)

print(ans)