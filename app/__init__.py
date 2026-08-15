import os
from flask import Flask
from app.routes import main


def create_app():
    app_dir = os.path.dirname(os.path.abspath(__file__))
    app = Flask(__name__,
                template_folder=os.path.join(app_dir, 'templates'),
                static_folder=os.path.join(app_dir, 'static'))
    app.register_blueprint(main)
    return app


app = create_app()