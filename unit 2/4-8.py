
for i in range(1,10):
    print(i+1)
    

for i in range(11,1,-1):
    print(i-1)

for i in range(1,50):
    if(i%2 != 0):
        print(i)

for i in range(0,5):
    for j in range(i):
        print("*",end=" ")
    print("\n")

for i in range(0,5):
    for s in range(5-i):
        print(" ",end=" ")
    for j in range(i):
        print(f" {i+j} ",end=" ")
    print()


for num in range(10, 51):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)
