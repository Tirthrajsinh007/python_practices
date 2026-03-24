# 16 Take a list of mixed elements and
# a. Write a lambda function to separate integer elements as an output list.
# b. Write another lambda function to separate string elements as an output
# list.

lst = [1,"tirth",2,"jayu",3,"gautam"]

withint = list(filter(lambda x: x if type(x) == int else 0,[x for x in lst]))
withString = list(filter(lambda x: x if type(x) == str else 0,[x for x in lst]))
print(withint)
print(withString)
