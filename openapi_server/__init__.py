import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from openapi_server.config import Config
from openapi_server.database import db
from openapi_server.encoder import JSONEncoder

def create_app():
    app = connexion.FlaskApp(__name__, specification_dir='./openapi/')
    
    # 配置应用
    app.app.config.from_object(Config)
    app.app.json_encoder = JSONEncoder
    
    # 初始化扩展
    db.init_app(app.app)
    CORS(app.app)
    Bcrypt(app.app)
    LoginManager(app.app)
    # 修改 Limiter 初始化方式
    Limiter(
        app=app.app,
        key_func=get_remote_address,
        default_limits=["200 per day", "50 per hour"]
    )
    
    # 添加API
    app.add_api('openapi.yaml', arguments={'title': '镜中CMS'})
    
    # 创建上传目录
    if not os.path.exists(app.app.config['UPLOAD_FOLDER']):
        os.makedirs(app.app.config['UPLOAD_FOLDER'])
    
    return app

app = create_app()

if __name__ == '__main__':
    app.run(port=8080)