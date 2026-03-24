# Take a string as an input and display the output to analysis the string based
# on separate words. Using map()
# a. Display the words in upper case along with the length of each word
# b. Display total number of each vowel in each word
# Eg. Str1 = ‘Hello how are you?’
# o/p: [{'a': 0, 'e': 1, 'length': 5}, {'a': 0, 'e': 0, 'length': 3}, {'a': 1, 'e': 1, 'length':
# 3}, {'a': 0, 'e': 0, 'length': 4}]

str1  = "Hello How are you?"
splitted = str1.split(' ')
ans = list(map(lambda x : {'a' :x.lower().count('a'),'b':x.lower().count('e'),'length':len(x)},splitted))
print(ans)




