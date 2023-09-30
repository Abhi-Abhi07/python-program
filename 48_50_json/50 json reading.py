import json

file=open("50 post.json", "r")

x=file.read()

finaldata=json.loads(x)
print(x)
print(type(x))
print()
print(finaldata)
print(type(finaldata))
# print(finaldata)
# print(type(finaldata))

# for a in finaldata:
#     print(a)
#
# for a in finaldata:
#     print(a['id'])