from flask import Flask
from PSIOT.config import Config
from flask_jwt_extended import JWTManager
from flask_cors import CORS


jwt = JWTManager()

def create_app(config_class=Config):
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(Config)  
      
    from PSIOT.NVR.routes import NVR
    from PSIOT.USER.routes import USER
    from PSIOT.home.routes import home
    from PSIOT.utils import mysql_connect

    jwt = JWTManager(app)    
    app.register_blueprint(home)
    app.register_blueprint(NVR,url_prefix='/nvr')
    app.register_blueprint(USER,url_prefix='/user')
    return app
