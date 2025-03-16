from flask import Blueprint, request, jsonify
from ..auth import install_admin, login
from ..database import db, User, Category, Article, Setting
from ..util import require_auth, sanitize_input
import bleach
from flask_bcrypt import Bcrypt
import os

bp = Blueprint('default', __name__)

bcrypt = Bcrypt()


@bp.route('/user/install', methods=['POST'])
def user_install_post():
    data = request.get_json()
    username = sanitize_input(data.get('username'))
    password = data.get('password')
    
    if not username or not password:
        return jsonify({'message': '用户名和密码不能为空'}), 400
    
    success, message = install_admin(username, password)
    if success:
        return jsonify({'message': message}), 200
    return jsonify({'message': message}), 400

@bp.route('/user/login', methods=['POST'])
def user_login_post():
    data = request.get_json()
    username = sanitize_input(data.get('username'))
    password = data.get('password')
    
    if not username or not password:
        return jsonify({'message': '用户名和密码不能为空'}), 400
    
    token, message = login(username, password)
    if token:
        return jsonify({
            'message': message,
            'token': token
        }), 200
    return jsonify({'message': message}), 401


@bp.route('/article/content', methods=['GET'])
@require_auth
def article_content_get():
    article_id = request.args.get('article_id', type=int)
    if not article_id:
        return jsonify({'message': '文章ID不能为空'}), 400
    
    article = Article.query.get(article_id)
    if not article:
        return jsonify({'message': '文章不存在'}), 404
    
    return jsonify({
        'article_id': article.article_id,
        'name': article.name,
        'content': article.content,
        'category_id': article.category_id
    }), 200

@bp.route('/article/del', methods=['POST'])
@require_auth
def article_del_post():
    article_id = request.args.get('article_id', type=int)
    if not article_id:
        return jsonify({'message': '文章ID不能为空'}), 400
    
    article = Article.query.get(article_id)
    if not article:
        return jsonify({'message': '文章不存在'}), 404
    
    try:
        db.session.delete(article)
        db.session.commit()
        return jsonify({'message': '文章删除成功'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': str(e)}), 500

@bp.route('/article/divide', methods=['POST'])
@require_auth
def article_divide_post():
    article_id = request.args.get('article_id', type=int)
    category_id = request.args.get('category_id', type=int)
    
    if not article_id or not category_id:
        return jsonify({'message': '文章ID和栏目ID不能为空'}), 400
    
    article = Article.query.get(article_id)
    if not article:
        return jsonify({'message': '文章不存在'}), 404
    
    category = Category.query.get(category_id)
    if not category:
        return jsonify({'message': '栏目不存在'}), 404
    
    try:
        article.category_id = category_id
        db.session.commit()
        return jsonify({'message': '文章划分成功'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': str(e)}), 500

@bp.route('/article/list', methods=['GET'])
@require_auth
def article_list_get():
    category_id = request.args.get('category_id', type=int)
    if not category_id:
        return jsonify({'message': '栏目ID不能为空'}), 400
    
    category = Category.query.get(category_id)
    if not category:
        return jsonify({'message': '栏目不存在'}), 404
    
    articles = Article.query.filter_by(category_id=category_id).all()
    return jsonify({
        'articles': [{
            'article_id': article.article_id,
            'name': article.name
        } for article in articles]
    }), 200


@bp.route('/category/add', methods=['POST'])
@require_auth
def category_add_post():
    data = request.get_json()
    name = sanitize_input(data.get('name'))
    
    if not name:
        return jsonify({'message': '栏目名称不能为空'}), 400
    
    try:
        category = Category(name=name)
        db.session.add(category)
        db.session.commit()
        return jsonify({'message': '栏目创建成功'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': str(e)}), 500

@bp.route('/category/del', methods=['POST'])
@require_auth
def category_del_post():
    category_id = request.args.get('category_id', type=int)
    if not category_id:
        return jsonify({'message': '栏目ID不能为空'}), 400
    
    category = Category.query.get(category_id)
    if not category:
        return jsonify({'message': '栏目不存在'}), 404
    
    if category.articles:
        return jsonify({'message': '栏目下存在文章，无法删除'}), 400
    
    try:
        db.session.delete(category)
        db.session.commit()
        return jsonify({'message': '栏目删除成功'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': str(e)}), 500

@bp.route('/category/list', methods=['GET'])
@require_auth
def category_list_get():
    categories = Category.query.all()
    return jsonify({
        'categories': [{
            'category_id': category.category_id,
            'name': category.name
        } for category in categories]
    }), 200


def file_download_post():  # noqa: E501
    """文件下载

     # noqa: E501


    :rtype: object
    """
    return 'do some magic!'


def file_upload_post(file=None):  # noqa: E501
    """文件上传

     # noqa: E501

    :param file: 
    :type file: str

    :rtype: InlineResponse2001
    """
    return 'do some magic!'


def system_add_post(key, value):  # noqa: E501
    """新增系统字段

     # noqa: E501

    :param key: 
    :type key: str
    :param value: 
    :type value: str

    :rtype: object
    """
    return 'do some magic!'


def system_del_post(key):  # noqa: E501
    """删除系统字段

     # noqa: E501

    :param key: 
    :type key: str

    :rtype: object
    """
    return 'do some magic!'


def system_list_get():  # noqa: E501
    """获取系统字段

     # noqa: E501


    :rtype: InlineResponse200
    """
    return 'do some magic!'


def system_update_post(key, value):  # noqa: E501
    """修改系统字段

     # noqa: E501

    :param key: 
    :type key: str
    :param value: 
    :type value: str

    :rtype: object
    """
    return 'do some magic!'


def install():
    """系统安装"""
    if User.query.first():
        return {"message": "系统已安装"}, 403
    
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return {"message": "参数错误"}, 400
    
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    user = User(username=username, password=hashed_password)
    
    db.session.add(user)
    db.session.commit()
    
    return {"message": "安装成功"}, 200

def article_add_post():
    """新增文章"""
    data = request.get_json()
    name = data.get('name')
    content = data.get('content')
    
    if not name or not content:
        return {"message": "参数错误"}, 400
    
    article = Article(name=name, content=content)
    db.session.add(article)
    db.session.commit()
    
    return {"message": "添加成功", "article_id": article.article_id}, 200
