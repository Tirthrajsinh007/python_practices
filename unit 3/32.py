# Take a list of words and print all palindrome words using filter() [Hint:
# string slicing str1[::-1]]

lst= ["pop","push","peep"];

ans = list(filter(lambda x: x == x[::-1],lst))
print(ans)