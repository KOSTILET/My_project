import random

# Функция для заполнения массива случайными числами
def fill_array(size, min_value, max_value):
    # Создаем массив заданного размера и заполняем случайными числами
    array = [random.randint(min_value, max_value) for _ in range(size)]
    return array

# Функция для вывода массива на экран
def print_array(array):
    # Преобразуем массив в строку и выводим
    array_str = ', '.join(map(str, array))
    print("Массив:", array_str)

# Пример использования функций
size = 10  # Размер массива
min_value = 1  # Минимальное значение для случайного числа
max_value = 100  # Максимальное значение для случайного числа

# Заполняем массив случайными значениями
array = fill_array(size, min_value, max_value)

# Выводим массив на экран
print_array(array)
