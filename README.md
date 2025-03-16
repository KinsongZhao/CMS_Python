# 镜中CMS

## 项目概述
镜中CMS 是一个轻量级的内容管理系统，基于 OpenAPI 规范开发，使用 Python Flask 和 Connexion 框架实现。系统提供了文章管理、栏目管理、文件处理等核心功能，适合小型网站或个人博客使用。

## 技术栈
- Python 3.8+
- Flask + Connexion
- MySQL 5.7
- OpenAPI 3.0 规范
- Swagger UI

## 环境要求
- Python 3.8 或更高版本
- pip 包管理器
- MySQL 5.7
- Windows/Linux/MacOS

## 目录结构

- mirror_cms/
  - openapi_server/            # 主程序目录
    - __init__.py
    - controllers/             # 控制器
      - __init__.py
      - default_controller.py
    - models/                  # 数据模型
      - __init__.py
      - base_model.py
    - openapi/                # API 规范文件
      - openapi.yaml
    - database/               # 数据库文件
      - cms.db
  - tests/                    # 测试用例
    - __init__.py
    - test_api.py
  - requirements.txt          # 依赖清单
  - README.md                 # 项目说明
  - .gitignore               # Git 忽略文件

## 快速开始

### 1. 安装依赖
```bash
pip install -r requirements.txt
```
### 2. 配置数据库
项目使用 MySQL 5.7 数据库，请确保：
1. MySQL 5.7 已正确安装并运行
2. 创建数据库：
```bash
mysql -u root -p
CREATE DATABASE mirror_cms CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```
3. 配置数据库连接信息（位于 config.py）：
```python
MYSQL_CONFIG = {
    'host': 'localhost',
    'port': 3306,
    'user': 'your_username',
    'password': 'your_password',
    'database': 'mirror_cms'
}
 ```


### 3. 运行服务器
```bash
python -m openapi_server
```
服务器默认运行在：

- 地址： http://127.0.0.1:12345
- Swagger UI： http://127.0.0.1:12345/ui/
- API 文档： http://127.0.0.1:12345/openapi.json

## 主要功能
### 系统管理
- 系统初始化
- 管理员账户设置
- 系统参数配置
### 内容管理
- 文章的增删改查
- 文章分类管理
- 栏目管理
- 文件上传下载
## API 文档
所有 API 接口都在 Swagger UI 中有详细说明，包括：

- 接口说明
- 请求参数
- 响应格式
- 示例数据
## 开发指南
### 添加新接口
1. 在 openapi/openapi.yaml 中定义接口规范
2. 在 controllers 目录下实现对应的处理函数
3. 在 models 目录下添加需要的数据模型
### 数据库操作
- 使用  MySQL 5.7 数据库
- 数据库文件位置： openapi_server/database/cms.db
- 表结构在首次运行时自动创建


## Docker 部署
### 构建镜像
```bash
docker build -t mirror_cms .
 ```

### 运行容器
```bash
docker run -d -p 12345:12345 -v /data/cms:/app/data mirror_cms
 ```


### 容器配置
- 端口映射：12345
- 数据持久化：/data/cms
## 常见问题
### 端口被占用
如遇端口冲突，可以修改 __main__.py 中的端口号：

```python
app.run(host='127.0.0.1', port=新端口号)
 ```


### 数据库访问错误
确保数据库目录具有读写权限：

```bash
chmod 755 openapi_server/database
chmod 644 openapi_server/database/cms.db
 ```


## 安全说明
- 建议在生产环境中修改默认端口
- 及时更新管理员密码
- 定期备份数据库文件
- 限制上传文件类型和大小
## 许可证
MIT License

