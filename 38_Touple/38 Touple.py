t=(10,20,20,20,30,40,50,)
t2=('py','php')
print(type(t))

a=t[1]
print(a)
print(t[3])

print("using length function")
for a in range (len(t)):
    print(t[a])

print("Direct pass")
for a in (t):
    print(a)

print()
print(max(t))
print(min(t))

print()
print(max(t2))
print(min(t2))

print()
print(t.count(20))
print(sum(t))

print()
print(sum(t,20)) # sum()function using two arguments
print(t.index(40))