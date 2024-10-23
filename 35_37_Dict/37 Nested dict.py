course={
    'php':{'duration':'2Month','fees':15000},
    'python':{'duration':'2Month','fees':10000},
    'java':{'duration':'3Month','fees':20000}
}

print(course)
print(course['php'])
print(course['php']['fees'])

# update
print()
course['java']['fees']=300000

print()
for a in course.items():
    print(a)

print()
for a,b in course.items():
    print(a,b)

print()
for a,b in course.items():
    print(a,b['duration'],b['fees'])

