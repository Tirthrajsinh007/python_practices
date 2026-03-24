# 15 Write a lambda function that takes one number and if the number is even,
# returns that number multiplied by 5 else if the number is odd, returns that
# number multiplied by 10

ans =  lambda x : x*5 if x%2 ==0 else x*10 if (x%2!=0) else 0

print(ans(10))

