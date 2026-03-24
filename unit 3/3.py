# Create functions to convert decimal numbers to binary, octal and
# hexadecimal numbers. Always return values from the functions

n = int(input("Enter decimal Number :"))
def binary():
    return print(bin(n)[2:])
def octal():
    return print(oct(n)[2:])
def hexadecimal():
    return print(hex(n)[2:])
    

binary()
octal()
hexadecimal()