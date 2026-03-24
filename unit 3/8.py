# 8. Write an UDF to check if the user given number is a prime number or not.

num = 12

def isprime(num):
    for y in range(3,9):
        if num%y == 0:
            return False;
        else:
            return True;
print(isprime(num))