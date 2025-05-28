from app import db
from werkzeug.security import generate_password_hash, check_password_hash

# 用户表
class User(db.Model):
    # 表名
    __tablename__ = 'users'

    # 字段定义
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(10), unique=True, nullable=False)
    user_id = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(20), unique=True, nullable=True)
    phone = db.Column(db.String(11), unique=True, nullable=True)
    avatar = db.Column(db.String(100), nullable=True)
    password = db.Column(db.String(10), nullable=False)
    password_hash = db.Column(db.String(320), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    update_at = db.Column(db.DateTime, server_default=db.func.now())
    def set_password(self, password):
        self.password = password
        self.password_hash = generate_password_hash(
            password, 
            method='pbkdf2:sha256:10000',  # 格式：算法:哈希方法:迭代次数
            salt_length=16
        )

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
    def __repr__(self):
        return f'<User {self.username}>'
    