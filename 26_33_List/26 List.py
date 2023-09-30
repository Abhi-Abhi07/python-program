# MUtable
# []
# Multiple value commas (,) separated

l=[10,30,40,25,"Hi",[1,3,2],35]
print(type(l))

# list slicing single value
# print(l[3],l[4])
print(l[3],l[4],l[5])
print(l[3],l[4],l[5][1])

# list slicing two argument
print(l[0:2])
print(l[3:])

# list slicing three argument
print()
print(l[0::2])

# reverse case always three argument
print(l[-1::-2])
print(l[-1::-1])

