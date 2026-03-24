#  Find the average of all the elements passed as an argument in lambda (using
# variable length arguments)


ans = lambda *a :sum(a)/len(a)

main =ans(10,20,30,40,50)
print(main)


