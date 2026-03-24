sal = int(input("Enter Salary :"))


tax = (
    0.5 if sal<30000 else
    0.15 if sal<30000 and sal>70000 else
    .25 
)

tax_rate = sal*tax
print("Tax is ",tax_rate)