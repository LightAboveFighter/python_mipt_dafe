from random import randint
a = [ [randint(-5, 5) for i in range(3) ] for k in range(3)]
print(a)
a = sorted(a, key=lambda x: x[1])
print(a)