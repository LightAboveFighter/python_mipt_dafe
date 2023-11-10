""" генератор range для чисел с плавающей точкой """

# Напишите генератор - аналог range, который генерирует арифметическую
# прогрессию, принимая 1, 2 или 3 аргумента:
#       - stop: последний (недостигаемый) член прогрессии
#       - start: первый член прогрессии (по умолчанию равен нулю) 
#       - step: шаг арифметической прогрессии (по умолчанию равен 1) 

def gen_progression(stop, start=0, step=1):
    actual_elem = start
    while True:
        yield actual_elem
        actual_elem += step
        if actual_elem >= stop:
            return "Арифметическая последовательность кончилась"

gap = gen_progression(36, 0, 5)
for i in range(9):
    print(next(gap))