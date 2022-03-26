# Windows-1251
import json
import logging

logging.basicConfig(filename='log.log', level=logging.ERROR)


def load_posts(path: str) -> list | None:
    """Загружает посты из json-файла"""
    try:
        with open(path, encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        logging.error("Ошибка доступа к файлу")
        return None
    except json.JSONDecodeError:
        logging.error('Файл не удается преобразовать')
        return None


def search_tag(posts: list, tag: str) -> list:
    """Выполняет поиск по слову"""
    return [post for post in posts if tag.lower() in post.get('content').lower()]


def update_data(path: str, data: list, new_data: dict):
    """Добавляет новый пост в список постов"""
    data.append(new_data)
    with open(path, 'w') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


def check_filename(filename: str) -> str | None:
    """Проверяет файл"""
    img_types = ('jpg', 'jpeg', 'jpe', 'gif', 'tif', 'tiff', 'png', 'bmp')
    extension = filename.split('.')[-1]
    if extension not in img_types:
        return extension
