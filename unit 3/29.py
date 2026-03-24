# Take 2 lists and add the elements of it if the 1st number is greater than the
# other else find the difference between them
# Eg. nums1 = [6, 5, 3, 9] nums2 = [0, 1, 7, 7]
# O/P [6, 4, 10, 2]

l1 = [6,5,3,9]
l2 = [0,1,7,7]


ans = list(map(lambda x,y:x+y if x<y else x-y,l1,l2))
print(ans)

