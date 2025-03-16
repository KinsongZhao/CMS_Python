#!/usr/bin/env python3

import connexion

from openapi_server import encoder


def main():
    app = connexion.App(__name__, specification_dir='./openapi/')
    app.app.json_encoder = encoder.JSONEncoder
    
    # 添加基本路由
    @app.app.route('/')
    def home():
        return app.app.redirect('/ui/')
    
    app.add_api('openapi.yaml',
                arguments={'title': '镜中CMS'},
                pythonic_params=True,
                options={
                    "serve_spec": True,
                    "swagger_ui": True,
                    "swagger_url": "/ui"
                })
    
    # 配置应用
    app.app.config['JSON_AS_ASCII'] = False
    app.app.config['DEBUG'] = True
    
    # CORS 支持
    @app.app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        return response
        
    app.run(host='127.0.0.1', port=12345)  # 修改为一个不常用的端口


if __name__ == '__main__':
    main()
