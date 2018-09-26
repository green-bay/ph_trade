import os
from flask import Flask, current_app, send_file
from flask_migrate import Migrate
from app.models import models

app = Flask(__name__, static_folder='../dist/static')

from .config import Config
app.logger.info(">>> {}".format(Config.FLASK_ENV))

db = models.db
db.init_app(app)

from .api import api_bp
app.register_blueprint(api_bp)

migrate = Migrate(app,db)

@app.route('/')
def index_client():
    dist_dir = current_app.config['DIST_DIR']
    entry = os.path.join(dist_dir, 'index.html')
    return send_file(entry)

