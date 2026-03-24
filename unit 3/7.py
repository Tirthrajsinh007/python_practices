# 7. Write a function to calculate total number of Uppercase and lowercase
# characters in the string.


str= "My Name is Tirth"
def upper_lower():
    
    lower_count = 0
    upper_count =0
    for i in str:
        if i.isupper():
            upper_count=upper_count+1;
        else:
            lower_count=lower_count+1;

    print(lower_count)
    print(upper_count)

upper_lower();

