from flask import current_app
from flask_bcrypt import Bcrypt
from datetime import datetime, timedelta
import jwt
from .database import db, User

bcrypt = Bcrypt()

def init_app(app):
    bcrypt.init_app(app)

def hash_password(password):
    return bcrypt.generate_password_hash(password).decode('utf-8')

def check_password(password_hash, password):
    return bcrypt.check_password_hash(password_hash, password)

def generate_token(user_id):
    payload = {
        'exp': datetime.utcnow() + timedelta(seconds=current_app.config['JWT_ACCESS_TOKEN_EXPIRES']),
        'iat': datetime.utcnow(),
        'sub': user_id
    }
    return jwt.encode(
        payload,
        current_app.config['JWT_SECRET_KEY'],
        algorithm='HS256'
    )

def verify_token(token):
    try:
        payload = jwt.decode(
            token,
            current_app.config['JWT_SECRET_KEY'],
            algorithms=['HS256']
        )
        return payload['sub']
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

from flask_bcrypt import Bcrypt
from .database import User, db
import jwt
import datetime

bcrypt = Bcrypt()
JWT_SECRET = 'your-secret-key'

def install_admin(username, password):
    if User.query.first():
        return False, "系统已安装"
    
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    user = User(username=username, password=hashed_password)
    
    try:
        db.session.add(user)
        db.session.commit()
        return True, "安装成功"
    except Exception as e:
        db.session.rollback()
        return False, str(e)

def login(username, password):
    user = User.query.filter_by(username=username).first()
    if not user:
        return None, "用户不存在"
    
    if not bcrypt.check_password_hash(user.password, password):
        return None, "密码错误"
    
    token = jwt.encode({
        'user_id': user.user_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
    }, JWT_SECRET, algorithm='HS256')
    
    return token, "登录成功"