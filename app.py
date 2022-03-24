from flask import Flask, request, render_template, send_from_directory, Blueprint
from functions import *

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)

posts = load_posts(POST_PATH)


@app.route("/")
def page_index():
    return render_template('index.html')


@app.route("/search")
def page_tag():
    s = request.args.get('s')
    post_list = search_tag(posts, s)
    return render_template('post_list.html', s=s, post_list=post_list)


@app.route("/post_uploaded", methods=["POST"])
def page_post_upload():
    pic = request.files.get('picture')
    text = request.form.get('content')
    return render_template('post_uploaded.html', picture=pic, text=text)


@app.route("/post_form", methods=["GET", "POST"])
def page_post_form():
    return render_template('post_form.html')


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


if __name__ == '__main__':
    app.run(debug=True)
