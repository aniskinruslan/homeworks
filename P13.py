from random import randrange
a = 10
b = 10
c = [randrange(1, 10) for i in range(a)]
d = [randrange(1, 15) for n in range(b)]
print(c)
print(d)
result = set(c).intersection(d)
print(result)
