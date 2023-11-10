""" Реализация своего контекстного менеджера. 

    Пусть в начале работы файла задаётся точность вычислений с 
    плавающей точкой (например, 3 знака после запятой)

    И пусть где-то по ходу выполнения программы нам необходимо
    повысить точность вычислений (например, до 6-ти знаков после запятой)

    Как это можно сделать?
"""

from contextlib import contextmanager       # для создания собственного контекстного менеджера
                                            # можно использовать декоратор @contextmanager
from decimal import Decimal, getcontext


# пример регулировки точности вычислений
getcontext().prec = 3

result = Decimal('104348') / Decimal('33215') 
print(result)

print("current precise:", getcontext().prec)

getcontext().prec = 15

result = Decimal('104348') / Decimal('33215') 
print(result)

print("current precise:", getcontext().prec)

#проблема такого решения заключается в том, что каждый раз переключая 
# точность вычислений, мы должны не забыть ее написать и уведомить 
# программиста/пользователя о использовании иной точности.
#  Писать такое количество строк кода также неприятно, поэтому испольхуем конструкцию with

#with func: 
#   <вычисления повышенной точности>

@contextmanager    #превращение нашего генератора в контекстный менеджер
def double_precision_mode():
    src_prec = getcontext().prec   #сохраняем исходную точность
    getcontext().prec = 2 * src_prec
    print("Double precision activated")
    yield
    getcontext().prec = src_prec
    print("Double precision desactivated")
    return 

#with запускает функцию при входе, и при выходе, поэтому у нас происходит
#  "включение" двойной точности, вычисление блока внутри with и выключение двойной точности

getcontext().prec = 3

#Вычисления обычной точности
result = Decimal('104348') / Decimal('33215') 
print(result)

#Вычисления повышенной точности
with double_precision_mode():
    result = Decimal('104348') / Decimal('33215') 
    print(result)

#Снова обычной
result = Decimal('104348') / Decimal('33215') 
print(result)

#как мы могли бы сделать:

def double2_precision_mode():
    src_prec = getcontext().prec   #сохраняем исходную точность
    getcontext().prec = 2 * src_prec
    print("Double precision activated")
    yield
    getcontext().prec = src_prec
    print("Double precision desactivated")
    return 
dpm = double2_precision_mode()

#обычная точность
result = Decimal('104348') / Decimal('33215') 
print(result)

#повышенная точность   -   аналог with в предыдущей реализии
next(dpm)
result = Decimal('104348') / Decimal('33215') 
print(result)
next(dpm)  #мы получим ошибку, с названием StopIteration
