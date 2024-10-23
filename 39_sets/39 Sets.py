s={10,20,30,40,50,30}
print(s)

# sets iteration using for loop
# print()
# for a in s:
#     print(a)

# # set() function
# # list, string, Touple convert into set
# l=[3,4,5,2,3]
# a=set(l)
# print(a)
#
# st="hfd,das,ds"
# print(set(st))
#
# t=(342,432,43,1,1,432)
# print(set(t))


# set() for dictionay
# d={
#     'name':'python',
#     'fees':'100',
#     'Duration':'2Month',
# }
# print(set(d['name']))
# print()
# course={
#     'php':{'duration':'2Month','fees':15000},
#     'python':{'duration':'2Month','fees':10000},
#     'java':{'duration':'3Month','fees':20000}
# }
# print(set(course))
# # print(course)


# s.remove(30)
# # print(s.remove(30)) # show error
# print(s)
#
# s.discard(20)
# print(s.discard(20)) # return none
# print(s)

# s.clear()
# print(s)

# s.pop()
# print(s)
# print(s.pop())
# print(s)
#
# s.add(3)
# s.add(3)
# print(s)
#
l=[100,200,30]
# s.update(23) # show error
s.update(l)
print(s)
