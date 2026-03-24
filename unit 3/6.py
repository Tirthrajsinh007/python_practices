# 6. Write a UDF to check the inputted number is between specified range or not. 

lst = [1,2,10,4,6]
num = 11

def ch(num):
    if num in lst:
        return True
    else:
        return False 

print(ch(num))
    
    