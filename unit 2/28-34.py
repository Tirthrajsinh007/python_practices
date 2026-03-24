str= "good morning!"
count =0
vovels = ('a','e','i','o','u')
for i in str:
    if i in vovels:
        count+=1
print(count)

t1 = ("Tirthrajsinh","p","Parmar")

t2 = (80,85,75,88,90,95)

# total with sum function
print(sum(t2))

# total without sum function
sum=0
for i in range(len(t2)):
    sum +=t2[i]
print(sum)

t3 = t1 +t2
print(t3)


# inp = int(input("Enter Number for search :"))
# if inp in t3:
#     print("found")
# else:
#     print("not found")
    
# fruits = ("apple","banana","orange","grapes","chikoo")

# inp_fruits = input("Enter Fruits nae for search :")

# if inp_fruits in fruits:
#     print("found")
# else:
#     print("not found")

# city = ()

# for i in range(1,3):
#     name = input("Enter city :")

# print(city)


