# 镜中CMS

## 项目概述
镜中CMS 是一个轻量级的内容管理系统，基于 OpenAPI 规范开发，使用 Python Flask 和 Connexion 框架实现。系统提供了文章管理、栏目管理、文件处理等核心功能，适合小型网站或个人博客使用。

## 技术栈
- Python 3.8+
- Flask + Connexion
- SQLite 数据库
- OpenAPI 3.0 规范
- Swagger UI

## 环境要求
- Python 3.8 或更高版本
- pip 包管理器
- SQLite 3.x
- Windows/Linux/MacOS

## 目录结构

## 安装依赖
```bash
pip install -r requirements.txt
python3 -m openapi_server
```

and open your browser to here:

```
http://localhost:8080/ui/
```

Your OpenAPI definition lives here:

```
http://localhost:8080/openapi.json
```

To launch the integration tests, use tox:
```
sudo pip install tox
tox
```

## Running with Docker

To run the server on a Docker container, please execute the following from the root directory:

```bash
# building the image
docker build -t openapi_server .

# starting up a container
docker run -p 8080:8080 openapi_server
```