""" Собственная реализация my_map() """

# примеры работы my_map()
print("Library map".center(30, "-"))
print()

vector1 = [3, 7, -2, 9, -3, 6]
squares = map(lambda x: x**2, vector1)
for num, sq in zip(vector1, squares):
    print(num, ":", sq, sep="\t")

print("".center(20, "-"))

vector2 = [3, -1, 0, 4]
prods = map(lambda x, y: x * y, vector1, vector2)
for num1, num2, pr in zip(vector1, vector2, prods):
    width = 2
    num1 = str(num1).center(width)
    num2 = str(num2).center(width)
    pr = str(pr).center(width)
    print(f"{num1} * {num2} = {pr}")

# Напишите функцию my_map, которая будет возвращать генератор
# результатов применения функции func к итерируемым объектам

print("My map".center(30, "-"))
print()


def my_map(func, *args):
    for elems in zip(*args):
        yield func(*elems)


vector1 = [3, 7, -2, 9, -3, 6]
squares = my_map(lambda x: x**2, vector1)
for num, sq in zip(vector1, squares):
    print(num, ":", sq, sep="\t")

print("".center(20, "-"))

vector2 = [3, -1, 0, 4]
prods = my_map(lambda x, y: x * y, vector1, vector2)
for num1, num2, pr in zip(vector1, vector2, prods):
    width = 2
    num1 = str(num1).center(width)
    num2 = str(num2).center(width)
    pr = str(pr).center(width)
    print(f"{num1} * {num2} = {pr}")