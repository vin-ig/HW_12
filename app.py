from flask import Flask
from main.main import main
from loader.loader import loader


app = Flask(__name__)

# Blueprint для главной станицы и поиска по словам
app.register_blueprint(main)

# Blueprint для добавления нового поста
app.register_blueprint(loader)

if __name__ == '__main__':
    # app.run(debug=True)
    app.run()
