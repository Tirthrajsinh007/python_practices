# Write a lambda function that will take 2 inputs. If inputs are integers, it will
# return the product of 2 numbers. Else perform concatenation.

ans = lambda x,y: x*y if type(x) == int and type(y) == int else str(x)+str(y)

print(ans(10,"hii"))
