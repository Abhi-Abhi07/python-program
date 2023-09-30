a="Abhishek"
n="123"
i="Abhi07"


print(a.find('h')) # start 0th index
print(a.find('h',5)) # start 5th index
print(a.find('hi')) # start 0th index and return first character index
print(a.find('he'))
print(a.find('y')) # y str me available nhi he so return (-1)

print("")
print(a.index('h'))
print(a.index('h',4))
print(a.index('hi'))
print(a.index('he'))
# print(a.index('y')) # y str me available nhi he show error

print("")
print("Abhishek isalpha() : ",(a.isalpha()))
print("123 isalpha() : ",n.isalpha())
print("Abhi07 isalpha() : ",i.isalpha())

print("")
print("Abhishek isdigit() : ",a.isdigit())
print("123 isdigit() : ",n.isdigit())
print("Abhi07 isdigit() : ",i.isdigit())

print("")
b="Abhi 07"
c="Abhi@07"
print("Abhishek isalnum() : ",(a.isalnum()))
print("123 isalnum() : ",n.isalnum())
print("Abhi07 isalnum() : ",i.isalnum())
print("Abhi 07 isalnum() : ",b.isalnum())
print(c.isalnum())