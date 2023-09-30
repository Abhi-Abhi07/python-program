import json

s='{"course":"python","duration":"2 Months"}'
# s='[{"course":"python","duration":"2 Months"}]'

j=json.loads(s)

print(j)
print(type(s))
print(type(j))

for a in j:
    print(a,j[a])
