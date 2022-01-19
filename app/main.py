#gunicorn -w 4 --reload -b localhost:5005 "app.main:create_app(testing=True)"

from flask import Flask
def create_app(testing: bool = True):
    app = Flask(__name__)

    @app.route("/")
    def index():
        return f"Hello world<br>Testing: {testing}<br>My name is Ankesh"

    return app
