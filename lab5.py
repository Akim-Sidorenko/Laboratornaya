"""
Вариант-6. Написать функцию, которая принимает путь к HTML
файлу и html тег («p», «h1», «article» и др.) и возвращает количество повторений полученного тега в файле с учетом того,
что требуется вернуть только количество тегов, который имеет открывающую и закрывающую часть.
"""

from bs4 import BeautifulSoup # Загружаем библиотеку bs4

"""
Функция ниже использует библиотеку bs4 и её класс BeautifulSoup для парсинга HTML-файла и поиска всех тегов
с заданным именем. И файл, и тег мы указываем ниже функции. Функция ищет у тега родительский элемент,
и если он есть, значит, у тега есть открывающая и закрывающая части. При этом функция увеличивает счётчик.
"""
def count_html_tags(file_path, tag_name):

    with open(file_path, 'r') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
        tag_list = soup.find_all(tag_name)
        count = 0
        for tag in tag_list:
            if tag.find_parent() is not None:
                count += 1
        return count

# указываем путь файла и нужный нам тег, я взял страницу гитхаба
count = count_html_tags('C:/Users/Eagle/Desktop/github_html.txt', 'div')
print(count)
