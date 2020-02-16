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
    from PSIOT.home.routes import home

    jwt = JWTManager(app)    
    app.register_blueprint(home)
    app.register_blueprint(NVR,url_prefix='/ps')
    return app
