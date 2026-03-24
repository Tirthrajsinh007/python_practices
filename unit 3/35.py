#  Take a matrix as input and transpose its elements using lambda
# Eg. matrix = [[1, 2],[3,4],[5,6],[7,8]]
#  o/p: [[1, 3, 5, 7], [2, 4, 6, 8]]

matrix = [[1, 2],[3,4],[5,6],[7,8]]
odd =[]
even =[]
ans = list(map(lambda x: list(x) ,zip(*matrix))
)
print(ans)
print(odd)
print(even)