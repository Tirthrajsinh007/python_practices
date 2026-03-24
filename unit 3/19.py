# From the provided list filter, the even numbers and odd numbers as a
# separate output list

lst =  [1,2,3,4,5,6,7,8,9]
odd = []
even = list(filter(lambda x: x if x%2==0 else odd.append(x),[x for x in range(10)]))
print(odd)
print(even)