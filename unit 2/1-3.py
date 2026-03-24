a= 50
b= 40
c= 30

# if(a>b):
#     print("a is max")
# else:
#     print("b is max")


# if(a<b):
#     print("a is min")
# else:
#     print("b is min")



if(a>b):
    print("a is max")
elif(b>c):
    print("b is max")
else:
    print("c is max")


if(a<b):
    print("a is min")
elif(b<c):
    print("b is min")
else:
    print("c is min")


basic = float(input("Enter basic salary: "))

if basic < 10000:
    da = basic * 0.25
    hra = basic * 0.05
elif basic >= 10000 and basic <= 30000:
    da = basic * 0.35
    hra = basic * 0.10
else:
    da = basic * 0.40
    hra = basic * 0.20

pf = basic * 0.12

net_salary = basic + da + hra - pf

print("Basic Salary:", basic)
print("DA:", da)
print("HRA:", hra)
print("PF:", pf)
print("Net Salary:", net_salary)
