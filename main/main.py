from flask import Blueprint, request, render_template
from functions import load_posts, search_tag
from config import POST_PATH
import logging

main = Blueprint('main', __name__, template_folder='templates')
logging.basicConfig(filename='../log.log', level=logging.INFO)


@main.route("/")
def page_index():
    """Главная страница"""
    return render_template('index.html')


@main.route("/search")
def page_tag():
    """Страница с результатами поиска по словам"""
    s = request.args.get('s')
    logging.info(s)  # Записываем в лог поисковые запросы
    posts = load_posts(POST_PATH)  # Загружаем список всех постов
    if posts:
        post_list = search_tag(posts, s)  # Ищем слово во всех постах
        return render_template('post_list.html', s=s, post_list=post_list)
    else:
        return render_template('main_error.html')
