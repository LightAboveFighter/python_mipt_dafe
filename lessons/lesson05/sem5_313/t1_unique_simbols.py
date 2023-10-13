"""
Задача 1: подсчёт количества уникальных символов в строке
"""

def unique(my_string: str) -> int:
    return len(set(my_string))
    """ Подсчёт количества уникальных символов в строке

        Вход:
            string: str
                исследуемая строка
        
        Выход:
            count: int
                количество уникальных символов в строке
    """
    pass

print(unique("erh"))
if __name__ == "__main__":
    pass
