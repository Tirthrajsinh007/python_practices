# 52 Read an existing file and take a user input string to be appended in that file.
# Also ask the position where new line need to be appended. Update the file
# content and print the updated file. [Hint: Make a file with new line character
# after each line]


f = open("d:\\one.txt","a+");
inp =input("Enter String :")
texts =f.readlines()
pos= int(input("Enter Position : "))
f.seek(0)
texts.insert(pos-1,inp)
copy =texts
f.writelines(copy)
print(f.readlines())




