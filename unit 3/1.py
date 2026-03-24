def mathematical() :
    a = int(input("Enter A :"))
    b = int(input("Enter B :"))
    n = input("Enter any of this sign to do operation")
    if n == '+':
        return print(a+b)
    if n == '-':
        return print(a-b)
    if n == '*':
        return print(a*b)
    if n == '/':
        return print(a/b)
    
mathematical();