import os
from flask import Flask, current_app, send_file
from flask_migrate import Migrate
from flask_login import LoginManager
from .config import Config

migrate = Migrate()
login_manager = LoginManager()
def create_app(config_obj=Config):
    app = Flask(__name__, static_folder='../dist/static')
    app.config.from_object(config_obj)

    from .db import db
    db.init_app(app)
    migrate.init_app(app,db)
    login_manager.init_app(app)

    from .api import api_bp
    app.register_blueprint(api_bp)

    @app.route('/')
    def index_client():
        dist_dir = current_app.config['DIST_DIR']
        entry = os.path.join(dist_dir, 'index.html')
        return send_file(entry)

    return app
