""" Файл содержит реализацию дополнительных функций для игры """

from random import randint
from os import system, name as os_name


def is_valid_value(value: int, number_characters: int) -> bool:
    """ Функция проверки числа на валидность

    :param value: число, которое необходимо проверить
    :param number_characters: кол-во разрядов, которое должно быть в данном числе
    :return: True - число валидно, False - число не валидно
    """

    output = False
    # Переводим value в обрабатываем вид
    value = 0 if value is None else int(abs(value))
    # Приводим number_characters в обрабатываемый вид
    number_characters = is_valid_input_number_character(number_characters)
    # Проверяем, что в числе необходимая разрядность, чем необходимо
    if 10**(number_characters - 1) <= value <= int('9' * number_characters):
        # Проверяем, что все цифры в числе разные
        value_list = list(str(value))
        value_set = set(value_list)
        if len(value_list) == len(value_set):
            output = True
    return output


def is_valid_input_number_character(number_character: int):
    """ Функция проеверки валидности входного параметра: разрядности загадываемого значения """
    if number_character is None or number_character == 0 or number_character < 0:
        raise ValueError("Введенное значение равно None, 0 или меньше 0")
    return int(number_character)


def generate_random_valid_value(number_characters: int) -> int:
    """ Функция генерации случайного валидного значения

    :param number_characters: кол-во разрядов у числа, которое необходимо сгенерировать
    :return: Сгенерированое значение
    """

    # Проверяем на валидность входной параметр
    number_characters = is_valid_input_number_character(number_characters)

    output = None
    number_characters = int(number_characters)
    # Формируем диапозон генерируемых чисел
    min_value = 10**(number_characters-1)
    max_value = int('9'*number_characters)
    # Генерируем валидное значение
    value = randint(min_value, max_value)
    while not is_valid_value(value, number_characters):
        value = randint(min_value, max_value)
    output = value
    return output


def cls():
    """ Функция отчиски консоли """
    system('cls' if os_name == 'nt' else 'clear')