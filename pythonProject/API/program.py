from flask import Flask
from API.Controllers.GamesController import games_bp
from API.Controllers.UsersController import user_bp

app = Flask(__name__)

app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(games_bp, url_prefix='/games')


if __name__ == '__main__':
    app.run()