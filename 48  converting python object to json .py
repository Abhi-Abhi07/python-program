import json

d={
    "course":"python",
    "fee":10000
}

j=json.dumps(d)

print(j)
print(type(d))
print(type(j))
