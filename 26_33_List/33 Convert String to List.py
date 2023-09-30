s=input("Enter the value ")
print(s)
l = s.split()
print(l)


l=[]
for a in range(1,4):
    n=input("Enter the value "+str(a)+" : ")
    l.append(n)
    # l.extend(n)
print(l)