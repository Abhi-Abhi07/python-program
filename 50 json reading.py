import json

file=open("post.json","r")

x=file.read()

finaldata=json.loads(x)

# print(finaldata)
# print(type(finaldata))

for a in finaldata:
    print(a)

for a in finaldata:
    print(a['id'])