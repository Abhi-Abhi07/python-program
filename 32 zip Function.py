l=[10,20,40,50]
l2=[3,5,77,88,8]

# zip extra elment ko ignore kar deta hai
for a,b in zip(l,l2):
    print(a,b)
#
for a, b in zip(l, l2):
    print(a+b)


# ek baar all output run karaye

# l=[10,20,40,50,4]
# l2=[3,5,77,88]
#
# l=[10,20,40,50]
# l2=[3,5,77,88,4]

# l=[10,20,40,50]
# l2=[3,5,77,88]
#
# t=len(l)
# for a in range(t):
#     print(l[a],l2[a])