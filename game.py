""" Файл содержит рерализацию самой игры """

import functions as f


def _welcome_game_print():
    """ Функция печати на экран сообщения о начале игры """
    print_str = "Игра \"Быки и коровы\"\n"
    print(print_str)


def _end_game_print():
    """ Функция печати на экран сообщения о завершении игры """
    print_str = "Поздравляю!!! Вы угадали число! Спасибо за игру!"
    print(print_str)


def get_input_user_value(text):
    """ Функция получения от пользователя значения """
    return input(text)


class Game:
    """ Класс, описывающий игру """

    def __input_user_value(self) -> bool:
        """ Функция, которая получает от пользователя число и порверяет его на валидность и если число валидное,
            то записывает его в соответствующее поле

            :return: Флаг валидности введенного значения
        """
        try:
            input_value = int(get_input_user_value("Введите число, которое задумал компьютер: "))
        except ValueError:
            f_output = False
        else:
            # Берем модуль числа на всякий случай
            input_value = abs(input_value)
            f_output = False
            if 10**(self.__number_character-1) <= input_value <= int(('9'*self.__number_character)):
                f_output = True
                self.__last_entered_value = input_value
        return f_output

    def __counter_bulls_cows(self):
        """ Метод подсчитывает кол-во коров и быков в веденном, пользователем, числе """
        # Перед подсчетом обнуляем кол-во быков и коров
        self.__count_bulls = 0
        self.__count_cows = 0
        # Формируем список из цифр для загаданного слова и введенного
        guess_number_lst = list(str(self.__guessed_number))
        entered_value_lst = list(str(self.__last_entered_value))
        # Перебираем загадываемое число
        for ind_guess in range(self.__number_character):
            number_guess = guess_number_lst[ind_guess]
            # Перебираем введенное число
            for ind_entered in range(self.__number_character):
                entered_number = entered_value_lst[ind_entered]
                # Условие быка
                if number_guess == entered_number and ind_guess == ind_entered:
                    self.__count_bulls += 1
                    # И заканчиваем вложенный цикл, т.к. все цифры в числе индивидуальны
                    break
                # Условие коровы
                elif number_guess == entered_number:
                    self.__count_cows += 1
                    # И заканчиваем вложенный цикл, т.к. все цифры в числе индивидуальны
                    break

    def __print_crows_bulls(self):
        """ Метод выводит на экран количество коров и быков в введенном числе """
        print(f"\nВы ввели значение: {self.__last_entered_value}. В нем {self.__count_bulls} быка и {self.__count_cows} коровы!\n")

    def __its_end_game(self) -> bool:
        """ Метод, который проверяет окончание игры? То, есть наличие 4х быков

            :return: True - игра окончена (пользователь угадал число), False - пользователь не угадал число
        """
        output = False
        if self.__count_bulls == self.__number_character:
            output = True
        return output

    def __init__(self, number_character: int):
        """ Конструктор

        :param number_character: разрядность загадываемого числа
        """

        # Разрядность загадываемого Числа
        self.__number_character = f.is_valid_input_number_character(number_character)
        self.__count_bulls = 0  # Количество быков
        self.__count_cows = 0  # Количество коров
        self.__guessed_number = None  # Загадываемое число
        self.__last_entered_value = None  # Последнее введенное число пользователем

    def start_game(self):
        """ Метод, который запускает игру """

        # Генерируем число
        self.__guessed_number = f.generate_random_valid_value(self.__number_character)

        while True:
            f.cls()
            _welcome_game_print()
            # Выведим число коров и быков
            self.__print_crows_bulls()
            # Просим пользователя ввести валидное число
            f_valid_value = self.__input_user_value()
            # Продолжаем, если число валидное
            if f_valid_value:
                # Подсчитываем кол-во коров и быков в числе
                self.__counter_bulls_cows()
                # Выведим число коров и быков
                self.__print_crows_bulls()
                # Определяем победил ли пользователь, если победил вывод соответствующее сообщение и заканчиваем игру
                f_end_game = self.__its_end_game()
                if f_end_game:
                    # Вызываем функцию печати о зварешении игры и заканчиваем игру
                    _end_game_print()
                    break
