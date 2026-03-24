# 51 Read 10th to 15th byte from the file and print.

with open("d:\one.txt") as f:
    f.seek(10)
    print(f.read(6));