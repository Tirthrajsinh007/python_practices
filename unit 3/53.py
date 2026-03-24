# 53 Read an alternate bytes/ character from the file.

with open("d:\\one.txt","+a") as f:
    f.seek(0)
    t= f.read()
    for i in range(t):
        print(i)
