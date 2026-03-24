# 50 Copy the content of one file to another

f= open("d:/one.txt","a+")
f.write("My name is tirth");
f.seek(0)
copy =f.read();
# print(f.read())

f1 =open("d:/two.txt","a+");
f1.write(copy)
f1.seek(0);
print(f1.read())

