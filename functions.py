import json
from pprint import pprint
# Windows-1251


def load_posts(path: str) -> list:
    """Загружает посты из json-файла"""
    try:
        with open(path, encoding='Windows-1251') as file:
            return json.load(file)
    except FileNotFoundError:
        print("Файл с постами не найден")
    except json.JSONDecodeError:
        print('Файл не удается преобразовать')


def search_tag(posts: list, tag: str) -> list | None:
    """Выполняет поиск по слову"""
    result = []
    for post in posts:
        if tag.lower() in post['content'].lower():
            result.append(post)
    if result:
        return result
    else:
        return None


def update_data(path: str, data: list, new_data: dict):
    """Добавляет новый пост в список постов"""
    data.append(new_data)
    try:
        with open(path, 'w') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
    except FileNotFoundError:
        print("Файл с постами не найден")


def check_file(file):
    """Проверяет файл"""
    img_types = ('jpg', 'jpeg', 'jpe', 'gif', 'tif', 'tiff', 'png', 'bmp')
    extension = file.filename.split('.')[-1]
    if extension not in img_types:
        return f'Тип файлов ".{extension}" не поддерживается, загрузите картинку'
    else:
        return 'Файл загружен!'
