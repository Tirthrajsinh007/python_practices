

binary = input("Enter a binary number: ")
octal = input("Enter an octal number: ")
hexadecimal = input("Enter a hexadecimal number: ")

decimal_from_binary = int(binary, 2)
decimal_from_octal = int(octal, 8)
decimal_from_hex = int(hexadecimal, 16)

print("Decimal from Binary:", decimal_from_binary)
print("Decimal from Octal:", decimal_from_octal)
print("Decimal from Hexadecimal:", decimal_from_hex)
