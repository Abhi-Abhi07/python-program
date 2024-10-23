# # del() Function use -> value DELETE
# # del index number par work karta he
# # del function ko print karane par error show karta he
# l=[2,5,10,20,34,90,23]
# # print(del(l[3])) -> show error
# del(l[3])
# print(l)

# # pop() Function use -> value DELETE
# # pop bhi index number par work karta he
# # differences b/w del() and pop() Function
# # del function ko print karane par error show karta he
# # pop function ko print karna par value return karta he
# l=[2,5,10,20,34,90,23]
# print(l.pop(3))
# l.pop(3)
# print(l)

# # remove Function use -> value DELETE
# # value par work karta he
# # remove function ko print karne par none return hota he
# l=[2,5,10,20,34,90,23]
# print(l.remove(20))
# l.remove(90)
# print(l)

# # clear Function use -> list ko empty karta he
# # clear function ko print karne par none return hota he
# l=[2,5,10,20,34,90,23]
# print(l.clear())
# l.clear() # return []
# print(l)

# # update Element from list
# l=[2,5,10,20,34,90,23]
# l[0]=3
# l[2]=100
# print(l)

# # insert function
# # (1,2)
# # 1. position
# # 2. value ya kya insert karna he
# # index number +ve he to left to right -> oth index =< position <= (last index + 1)
# # position > (last index + 1) to value ko last me hi add karega
# # index number -ve he to right to left -> last index(-1) => position >= first index (len(list))
# # position < first index (len(list)) => postion => to value starting me add hogi
# l=[2,5,10,20,34,90,23]
# print(len(l))
# l.insert(0,21)
# print(l)

# append Function use -> data ko add karta he
# l=[2,5,10,20,34,90,23]
# l.append([7,8,9])
# l.append(300)
# print(l)

# extends Function use -> value ko add karta he
l=[2,5,10,20,34,90,23]
l.extend([7,8,9])
l.extend(["ghu"])
print(l)
