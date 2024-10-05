a = type(1)
print(a)

b = type(1.1)
print(b)

c = type("Hello")
print(c)

d = type(True)
print(d)

e = type(None)
print(e)


f = type("99")  # f is a string
print(f)

f = "99"
g = float(f)  # making f, which is a str, into float by using float()
g = type(g)
print(g)
