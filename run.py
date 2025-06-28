from flask import Flask
from app.routes import main as routes

app = Flask(__name__)

if __name__ == '__main__':
    app.register_blueprint(routes)
    app.run(debug=True)