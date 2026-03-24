# 4. Write an UDF to return a list having only unique values by removing
# duplicate values from the provided input list


def unique_list(lst):
    new =[]
    for i in lst:
        if i not in new:
            new.append(i)
    return new
item= [1,2,2,3,4,4]
print(unique_list(item))     