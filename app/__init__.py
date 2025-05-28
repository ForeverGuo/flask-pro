from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv

load_dotenv() 

# 创建扩展对象
db = SQLAlchemy()
def create_app(config_name=None):
    # 创建 Flask 应用程序实例
    app = Flask(__name__)

    # 加载配置
    if config_name is None:
        app.config.from_object('config.DevelopmentConfig')  # 默认加载开发环境配置
    else:
        app.config.from_object(f'config.{config_name}')  # 根据参数加载配置

    # 初始化扩展
    db.init_app(app)

    # migrate db
    migrate = Migrate(app, db)

    # jwt验证
    jwt = JWTManager(app)

    from .models.admin import User, category, Product
    # # 创建数据库表 (如果表不存在)
    with app.app_context():
        # 创建所有表
        db.create_all()

    return app, jwt