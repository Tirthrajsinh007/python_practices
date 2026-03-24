# 36 Find the factorial of a number using lambda (recursive)

def fact(num):
    while num==0:
        return 1;
    else  :
        return num *fact(num-1);

print(fact(5))