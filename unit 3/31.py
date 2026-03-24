# Take a list of floating-point numbers and display list of all round numbers.
# Also round them with just 2 decimal points. Using map()
# Eg. [6.56773, 9.57668, 4.00914, 56.24241, 9.01344]

n = [6.56773, 9.57668, 4.00914, 56.24241, 9.01344]

ans = list(map(lambda x: round(x),n))
ans2 = list(map(lambda x: round(x,2),n))
print(ans)
print(ans2)






