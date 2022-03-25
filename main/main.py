from flask import Blueprint, request, render_template
from functions import *
from config import POST_PATH

main = Blueprint('main', __name__, template_folder='templates')

posts = load_posts(POST_PATH)


@main.route("/")
def page_index():
    """Главная страница"""
    return render_template('index.html')


@main.route("/search")
def page_tag():
    """Страница с результатами поиска по словам"""
    s = request.args.get('s')
    post_list = search_tag(posts, s)
    return render_template('post_list.html', s=s, post_list=post_list)
