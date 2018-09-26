import os 
from app import app 

class Config(object): 
    FLASK_ENV = os.getenv('FLASK_ENV', 'production') 
    SECRET_KEY = os.getenv('FLASK_SECRET', 'Nothing2hide') 
    APP_DIR = os.path.dirname(__file__) 
    ROOT_DIR = os.path.dirname(APP_DIR) 
    DIST_DIR = os.path.join(ROOT_DIR, 'dist') 
    DB_NAME = os.getenv('DB_NAME', 'ph_trade') 
    SQLALCHEMY_DATABASE_URI = 'postgresql://ph_trade:ph_trade@localhost/ph_trade'
    BCRYPT_LOG_ROUNDS = os.getenv('BRYCPT_LOG_ROUNDS', 12)
    
    if not os.path.exists(DIST_DIR): 
        raise Exception('DIST_DIR not found {}'.format(DIST_DIR)) 

class ConfigTest(Config):
    DB_NAME = 'ph_trade_test'
    BCRYPT_LOG_ROUNDS = 5

app.config.from_object('app.config.Config')
