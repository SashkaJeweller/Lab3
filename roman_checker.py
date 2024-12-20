import re
import requests

# Регулярное выражение для римских чисел
roman_regex = re.compile(r"M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})")


def is_valid_roman(roman):
    return bool(roman_regex.fullmatch(roman))


def search_roman_in_text(text):
    return roman_regex.findall(text)


def search_roman_in_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    return search_roman_in_text(content)


def search_roman_in_url(url):
    response = requests.get(url)
    response.raise_for_status()
    return search_roman_in_text(response.text)


if __name__ == "__main__":
    # Пользовательский ввод
    user_input = input("Введите римское число: ")
    if is_valid_roman(user_input):
        print(f"{user_input} является корректным римским числом.")
    else:
        print(f"{user_input} не является корректным римским числом.")

    # Пример использования поиска в файле или по URL Можно раскомментировать для работы
    # print(search_roman_in_file('path/to/your/file.txt'))
    # print(search_roman_in_url('http://example.com'))

