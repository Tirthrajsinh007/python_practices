#  Filter all vowels from the given string

str1 = "my name is tirth"

ans = list(filter(lambda x: x if x == 'a' or x =='e'or x=='i' or x=='o' or x=='u' else 0,[x for x in str1])
)
print(ans)