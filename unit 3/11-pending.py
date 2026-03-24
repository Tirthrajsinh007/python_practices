num = 10

ans = lambda x:x>1 and all(num%i!=0 for i in range(2,num**0.5))

print(ans)