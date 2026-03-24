num =1634
num_len = len(str(num))
temp = num
sum =0
while(temp>0):
    r = temp%10;
    print(r)
    sum = sum+(r**num_len)
    print(sum)
    temp//=10

if(num == sum ):
    print("Armstrong number ")
else:
    print("Not Armstrong number")