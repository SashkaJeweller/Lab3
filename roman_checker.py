import re


# Функция для проверки корректности римского числа
def is_valid_roman(roman):
    # Регулярное выражение для проверки римских чисел
    pattern = r"^(M{0,3})(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
    return re.match(pattern, roman) is not None


# Функция для поиска всех римских чисел в тексте
def find_roman_numerals(text):
    # Регулярное выражение для поиска римских чисел
    pattern = r"\b(M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3}))\b"
    return re.findall(pattern, text)


# Основная программа
if __name__ == "__main__":
    # Ввод текста от пользователя
    input_text = input("Введите текст для поиска римских чисел: ")

    # Поиск римских чисел в тексте
    found_numerals = find_roman_numerals(input_text)

    # Вывод найденных римских чисел
    if found_numerals:
        print("Найденные римские числа:")
        for numeral in found_numerals:
            print(numeral[0])  # Выводим только первое совпадение
    else:
        print("Римские числа не найдены.")

    # Проверка на корректность римского числа
    roman_input = input("Введите римское число для проверки: ")
    if is_valid_roman(roman_input):
        print(f"{roman_input} является корректным римским числом.")
    else:
        print(f"{roman_input} не является корректным римским числом.")
