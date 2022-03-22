import unittest

import functions as gf


class IsValidValueTest(unittest.TestCase):
    """ Тесты для функции проверки валидности числа """

    def setUp(self) -> None:
        self.value_std = 1234
        self.number_character_std = 4

    def test_value_None(self):
        """ В качестве значение передается None """
        result = gf.is_valid_value(None, self.number_character_std)
        self.assertFalse(result)

    def test_number_character_None(self):
        """ В качестве размерности числа передается None """
        with self.assertRaises(ValueError):
            result = gf.is_valid_value(self.value_std, None)

    def test_value_with_wrong_number_character(self):
        """ Тест, при котором значение пеередается вне диапозона размерности чисел """
        value_less = 999
        value_more = 10000
        # Меньше
        result = gf.is_valid_value(value_less, self.number_character_std)
        self.assertFalse(result)
        # Больше
        result = gf.is_valid_value(value_more, self.number_character_std)
        self.assertFalse(result)

    def test_same_numbers_in_value(self):
        """ Присутствие одинаковых цифр в числе не проходят валидность """
        value_2 = 1123
        value_3 = 1112
        value_4 = 1111

        result = gf.is_valid_value(value_2, self.number_character_std)
        self.assertFalse(result)
        result = gf.is_valid_value(value_3, self.number_character_std)
        self.assertFalse(result)
        result = gf.is_valid_value(value_4, self.number_character_std)
        self.assertFalse(result)

    def test_value_float(self):
        """ Тип данных у проверяемого числа float """
        value_1 = 1234.56
        value_2 = 999.9

        result = gf.is_valid_value(value_1, self.number_character_std)
        self.assertTrue(result)
        result = gf.is_valid_value(value_2, self.number_character_std)
        self.assertFalse(result)

    def test_character_float_value(self):
        """ Тип данных у переменной, которая отвечает за разрядность числа, является float """
        number_character_1 = 4.6
        number_character_2 = 3.6

        result = gf.is_valid_value(self.value_std, number_character_1)
        self.assertTrue(result)
        result = gf.is_valid_value(self.value_std, number_character_2)
        self.assertFalse(result)

    def test_input_parameters_less_0(self):
        """ Входные параметры в функции меньше 0 """
        value = -1234
        number_character = -4

        result = gf.is_valid_value(value, self.number_character_std)
        self.assertTrue(result)
        with self.assertRaises(ValueError):
            result = gf.is_valid_value(value, number_character)

    def test_valid_values(self):
        """ Тест с валидными данными """
        value_1 = 3
        number_character_1 = 1
        value_2 = 12345678
        number_character_2 = 8

        result = gf.is_valid_value(value_1, number_character_1)
        self.assertTrue(result)
        result = gf.is_valid_value(value_2, number_character_2)
        self.assertTrue(result)
        result = gf.is_valid_value(self.value_std, self.number_character_std)
        self.assertTrue(result)


class IsValidInputNumberCharacterTest(unittest.TestCase):
    """ Тест для функции проеверки валидности входного параметра: разрядности загадываемого значения """

    def test_not_valid_value(self):
        """ Проверка работоспособности функции при не валидном значении """
        value_1 = None
        value_2 = 0
        value_3 = -3

        with self.assertRaises(ValueError):
            gf.is_valid_input_number_character(value_1)
            gf.is_valid_input_number_character(value_2)
            gf.is_valid_input_number_character(value_3)

    def test_float_value(self):
        """ Проверка работоспособности функции при передачи в нее тип данных типа float """
        value_1 = 3.6
        value_2 = 4.4

        result = gf.is_valid_input_number_character(value_1)
        self.assertEqual(result, int(value_1))
        result = gf.is_valid_input_number_character(value_2)
        self.assertEqual(result, int(value_2))

    def test_valid_value(self):
        """ Проверка работоспособности функции при передачи валидного значения """
        value = 5

        result = gf.is_valid_input_number_character(value)
        self.assertEqual(result, value)


class GenerateRandomValidValueTest(unittest.TestCase):
    """ Тест для функции генерации валидного случайного числа """

    def test_valid_number_character(self):
        """ Проверка работоспособности функции при передачи в нее None и 0 """
        number_character_none = None
        number_character_null = 0

        with self.assertRaises(ValueError):
            result = gf.generate_random_valid_value(number_character_none)
            result = gf.generate_random_valid_value(number_character_null)

    def test_number_character_less_0(self):
        """ Проверка работоспособности функции при передачи в нее отрицательного значения """
        number_character = -4
        with self.assertRaises(ValueError):
            result = gf.generate_random_valid_value(number_character)

    def test_character_float_value(self):
        """ Тип данных, у входного параметра, является float """
        number_character_1 = 4.6
        number_character_2 = 3.6

        result = gf.generate_random_valid_value(number_character_1)
        self.assertTrue(gf.is_valid_value(result, number_character_1))
        result = gf.generate_random_valid_value(number_character_2)
        self.assertTrue(gf.is_valid_value(result, number_character_2))

    def test_valid_values(self):
        """ Проверяем валидность сгенерированных чисел """
        number_character_lst = [2, 4, 8]

        # Генериуем числа и проверяем их валидность
        for number_character in number_character_lst:
            value = gf.generate_random_valid_value(number_character)
            result = gf.is_valid_value(value, number_character)
            self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
