from flask import Flask, send_from_directory
from main.main import main
from loader.loader import loader


app = Flask(__name__)

# Blueprint для главной станицы и поиска по словам
app.register_blueprint(main)

# Blueprint для добавления нового поста
app.register_blueprint(loader)


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


if __name__ == '__main__':
    app.run()
