from flask import Flask
from main.main import main
from loader.loader import loader


app = Flask(__name__)
app.register_blueprint(main)
app.register_blueprint(loader)

if __name__ == '__main__':
    app.run(debug=True)
