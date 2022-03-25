from flask import Blueprint, request, render_template, send_from_directory
from functions import *
from config import POST_PATH, UPLOAD_FOLDER

loader = Blueprint('loader', __name__, template_folder='templates')

posts = load_posts(POST_PATH)


@loader.route("/post_uploaded", methods=["POST"])
def page_post_upload():
    """Страница с загруженным постом"""
    picture = request.files.get('picture')  # Получаем картинку из формы
    pic_path = UPLOAD_FOLDER + picture.filename  # Путь к картинке на диске
    picture.save(pic_path)  # Сохраняем картинку
    # Проверяем загруженный файл
    text = request.form.get('content')  # Получаем текст поста
    update_data(POST_PATH, posts, {"pic": pic_path, "content": text})   # Обновляем список постов
    return render_template('post_uploaded.html', picture=pic_path, text=text)


@loader.route("/post_form", methods=["GET", "POST"])
def page_post_form():
    """Страница с добавлением поста"""
    return render_template('post_form.html')


@loader.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)
