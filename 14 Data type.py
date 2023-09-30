a=5
print(a,"is of type",type(a)) # int
a=4.5
print(a,"is type of",type(a)) # float
a=4+7j
print(a,"is type of",type(a)) # complex

print()
# String
print("String")
s="This is a string"
print(s,"is type of",type(s))

s='''
    Abhi
    07
    Bhai
'''
print(s,"is type of",type(s))

s='10'
print(s,"is type of",type(s))

print()
# List is Mutable
print("List")
l=[1,2,3.4,'Ab',4+8j]
print(l,"is type of",type(l))
l[2]=10
print(l,"is type of",type(l))

print()
# Touple are immutable
print("Tuple")
t=(10,23,'Ab',4+8j)
print(t,"is type of",type(t))
# t[1]=4 # show error

print()
# Dictionary are mutable
print("Dictionary")
# Dict me key always different hoti he but value same ho sakti he
d={
    'Language':'python', # language -> key & python -> value
    'Learn':'wscubetech' # Learn -> key & wscubetech -> value
}
print(d['Language']) # get value of Language
print(d,"is type of",type(d))

print()
# Set are immutable
# unique element ( no duplicate )
print("Set")
s={10,10,10,2,34}
print(s,"is type of",type(s))

