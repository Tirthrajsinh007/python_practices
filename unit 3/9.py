# 9. Write a findString() function to find all the positions of occurrences of
# string2 in string1 and return that value. If string2 is not present in string1
# then display suitable message.
# Eg. Str1 = Hello all, Good Morning to all. (pass it as a parameter in the
# function)
#  Str2 = ‘all’ (pass it as a parameter, but f not passed take a default
# argument)
# O/p: String 2 found at positions: [6, 27]


str1= "Hello all, Good  Morning to all"
str2 = "all"



def findString(str1,str2):
    l1 =[]
    i = 0;
    while True:
        i= str1.find(str2,i)
        if i == -1 :
            break;
            
        l1.append(i)
        i =i+len(str2)
        
    print(l1)
findString(str1,str2)
