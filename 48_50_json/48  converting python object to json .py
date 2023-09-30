import json

d={
    "course":"python",
    "fee":10000
}

j=json.dumps(d)

print(j)
print(type(j))
print(d)
print(type(d))