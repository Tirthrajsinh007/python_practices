# Eg. GeneratePrime(10) function will return 1st 10 prime numbers starting
# from 2 like 2,3,5,7,11,13,15,1719,23

def generatePrime(n):
    i =2
    lst = []
    while len(lst) < n:
        prime =True
        for j in range(2,int(i**0.5)+1):
            if i%j ==0:
                prime =False
                break;
        if prime ==True:
            lst.append(i)
        i+=1;
    return lst    

print(generatePrime(10))