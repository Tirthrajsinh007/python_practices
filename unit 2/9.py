num = int(input("Enter Number to check : "))
temp = num
rev=0
if(len(str(num)) >3):
    while(temp>0):
        r= temp%10;
        rev = (rev*10)+r;
        temp = temp//10
    
    if(rev == num):
        print("palindrome")
    else:
        print("not palindrome")

else:
    print("Enter More bigger number ")

