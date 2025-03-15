import os

class Config:
    # 基础配置
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev'
    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    
    # 数据库配置
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost:3306/cms?charset=utf8mb4'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # 安全配置
    SESSION_COOKIE_SECURE = True
    REMEMBER_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    
    # CORS配置
    CORS_HEADERS = 'Content-Type'
    
    # 文件上传配置
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB
    UPLOAD_FOLDER = os.path.join(BASEDIR, 'uploads')
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
    
    # JWT配置
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'jwt-secret-key'
    JWT_ACCESS_TOKEN_EXPIRES = 3600  # 1小时
    
    # 速率限制
    RATELIMIT_DEFAULT = "200 per day;50 per hour"
    RATELIMIT_STORAGE_URL = "memory://"
    
    # 内容安全配置
    MAX_USERNAME_LENGTH = 10
    MAX_PASSWORD_LENGTH = 20
    MAX_CONTENT_LENGTH_MB = 16
    
    @staticmethod
    def init_app(app):
        # 创建上传文件夹
        if not os.path.exists(Config.UPLOAD_FOLDER):
            os.makedirs(Config.UPLOAD_FOLDER)