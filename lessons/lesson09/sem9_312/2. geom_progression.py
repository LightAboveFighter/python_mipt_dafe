""" ГЕОМЕТРИЧЕСКАЯ ПРОГРЕССИЯ """
 
# Напишите бесконечный генератор геометрической прогрессии.
# В качестве параметров генератор должен принимать:
#       - первый член прогрессии
#       - шаг прогрессии

def geo_progression_generator(start = 1, step = 1):
    actual_elem = start
    while True:
        yield actual_elem
        actual_elem *= step

ggp = geo_progression_generator(2, 2)
for _ in range(5):
    print(next(ggp))
for _ in range(5):
    print( 0.7 + next(ggp))
