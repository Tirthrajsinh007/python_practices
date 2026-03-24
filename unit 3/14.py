# Create a lambda function that will return maximum of three numbers

ans = lambda x,y,z: x if x>y and x>z else (y if (y>x and y>z) else c)

print(ans(11,3,2))

