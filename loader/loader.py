from flask import Blueprint, request, render_template
from functions import load_posts, update_data, check_filename
from config import POST_PATH, UPLOAD_FOLDER
import logging

loader = Blueprint('loader', __name__, url_prefix='/post', template_folder='templates')
logging.basicConfig(filename='../log.log', level=logging.INFO)


@loader.route("/uploaded", methods=["POST"])
def page_post_upload():
    """Страница с загруженным постом"""
    # Загружаем файл с постами и исключаем ошибку
    posts = load_posts(POST_PATH)
    if not posts:
        return render_template('loader_error.html', message='Ошибка загрузки данных')

    # Получаем картинку из формы
    picture = request.files.get('picture')

    # Проверяем расширение файла
    check = check_filename(picture.filename)
    if check:
        message = f'Тип файлов ".{check}" не поддерживается'
        logging.info(message)
        return render_template('loader_error.html', message=message)

    # Исключаем ошибку загрузки нового поста
    try:
        pic_path = UPLOAD_FOLDER + picture.filename  # Путь к картинке на диске
        picture.save(pic_path)  # Сохраняем картинку
        text = request.form.get('content')  # Получаем текст поста
    except FileNotFoundError:
        return render_template('loader_error.html', message='При добавлении поста произошла ошибка')
    except (PermissionError, IsADirectoryError):
        return render_template('loader_error.html', message='Без изображения пост добавить нельзя')

    # Если все прошло успешно, показываем загруженный пост
    update_data(POST_PATH, posts, {"pic": pic_path, "content": text})  # Обновляем список постов
    return render_template('post_uploaded.html', picture=pic_path, text=text)


@loader.route("/form", methods=["GET", "POST"])
def page_post_form():
    """Страница с добавлением поста"""
    return render_template('post_form.html')
