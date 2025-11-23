from app import app
from app.routes import main

if __name__ == '__main__':
    app.register_blueprint(main)
    app.run(debug=True)