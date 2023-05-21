s="What {} to do {} or think".format(20,"hello")
print(s)

s="What {} to {} do {} {} or think".format(100,20,"hello","you")
print(s)

s="What {0} to do {1} or think".format(20,"hello")
print(s)

s="What {1} to do {0} or think".format(20,"hello")
print(s)

st="Kya chal rha {2} {0} {1} he".format(0,1,2)
print(st)

s="What {ab} to {ac} do or think".format(ab=100,ac=20,z="hello")
print(s)


# {a:10} show character space for 10 character
s="what {a:10} to do".format(a=20)
print(s)

# ^ value in the mid
s="what {a:^10} to do".format(a=209)
print(s)


# < value first then character space
s="what {a:<10} to do".format(a=20)
print(s)

# > character space then value last
s="what {a:>10} to do".format(a=20)
print(s)

