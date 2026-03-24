# 5. Write a Python function to multiply all the numbers in a list.

lst = [1,2,3,4,5,6,7,8,9]


def multiply(ls):
    sum =1
    for i in ls:
        sum = sum*i
    return print(sum)

multiply(lst)