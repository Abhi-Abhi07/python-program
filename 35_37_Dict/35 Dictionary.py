d={
    'name':'python',
    'fees':100,
    'Duration':'2Month',
}
print(d)
print(type(d))

a='name'
print(d[a])

print(d['Duration'])

print()
for a in d:
    print(a) # key return

print()
for a in d:
    print(d[a]) # value return