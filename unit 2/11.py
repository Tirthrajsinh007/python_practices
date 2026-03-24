n = int(input("Enter number of Elements you eant to enter :"))

numbers = tuple(int(input("Enter element :")) for i  in range(n))


even_count = 0;
odd_count = 0;

for i in numbers:
    if i%2 == 0:
        even_count+=1
    else:
        odd_count+=1

print("Odd Count is :",odd_count)
print("Even count is  :",even_count)