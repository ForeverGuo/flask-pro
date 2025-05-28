import os
from datetime import timedelta

class Config:
    # 通用配置
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # mysql 配置
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 禁用事件系统
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_size': 20,          # 连接池大小
        'pool_recycle': 300,      # 连接回收时间(秒)
        'pool_pre_ping': True     # 执行前检查连接有效性
    }
class DevelopmentConfig(Config):
    # 开发环境配置
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=1)

class TestingConfig(Config):
    # 测试环境配置
    TESTING = True
    SQLALCHEMY_DATABASE_URI = ''
    JWT_SECRET_KEY = 'secret'

class ProductionConfig(Config):
    # 生产环境配置
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', '')