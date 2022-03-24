import json
from pprint import pprint


def load_posts(path):
    with open(path, encoding='utf-8') as file:
        return json.load(file)


def search_tag(posts, tag):
    result = []
    for post in posts:
        if tag.lower() in post['content']:
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

# file = FileStorage('D:\Temp\posts.json')
# data = load_posts('posts.json')

# pprint(search_tag(data, 'вижу'))
# picture = request.files.get('picture')
# picture.save(f'./uploads/{picture.filename}')
