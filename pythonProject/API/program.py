from flask import Flask
from flask_cors import CORS
from API.Controllers.GamesController import games_bp
from API.Controllers.LaunchersController import launcher_bp
from API.Controllers.UsersController import user_bp
from API.Controllers.TagsController import tags_bp

app = Flask(__name__)

CORS(app, origins=["http://localhost:5173"], methods=["GET", "POST", "PUT", "DELETE"])

app.register_blueprint(user_bp, url_prefix='/api/users')
app.register_blueprint(games_bp, url_prefix='/api/games')
app.register_blueprint(tags_bp, url_prefix='/api/tags')
app.register_blueprint(launcher_bp, url_prefix='/api/launcher')


if __name__ == '__main__':
    app.run()