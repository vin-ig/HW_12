import json
from pprint import pprint
# Windows-1251


def load_posts(path: str) -> list:
    with open(path, encoding='Windows-1251') as file:
        return json.load(file)


def search_tag(posts: list, tag: str) -> list:
    result = []
    for post in posts:
        if tag.lower() in post['content'].lower():
            result.append(post)
    return result


def update_data(path: str, data: list, new_data: dict):
    data.append(new_data)
    with open(path, 'w') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


def check_file(file):
    img_types = ('jpg', 'jpeg', 'jpe', 'gif', 'tif', 'tiff', 'png', 'bmp')
    extension = file.filename.split('.')[-1]
    if extension not in img_types:
        return f'Тип файлов ".{extension}" не поддерживается, загрузите картинку'
    else:
        return 'Файл загружен!'
