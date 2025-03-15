from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='用户ID')
    username = db.Column(db.String(10), unique=True, nullable=False, comment='用户名')
    password = db.Column(db.String(60), nullable=False, comment='密码')

class Category(db.Model):
    __tablename__ = 'category'
    category_id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='栏目ID')
    name = db.Column(db.String(50), nullable=False, comment='栏目名称')
    articles = db.relationship('Article', backref='category', lazy=True)

class Article(db.Model):
    __tablename__ = 'article'
    article_id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='文章ID')
    category_id = db.Column(db.Integer, db.ForeignKey('category.category_id'), comment='所属栏目ID')
    name = db.Column(db.String(50), nullable=False, comment='文章标题')
    content = db.Column(db.Text, comment='文章内容')

class Setting(db.Model):
    __tablename__ = 'setting'
    key = db.Column(db.String(50), primary_key=True, comment='配置键名')
    value = db.Column(db.String(500), comment='配置值')