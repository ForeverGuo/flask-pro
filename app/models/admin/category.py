from unicodedata import category
from app import db

"""
  商品分类表
  id: 分类id
  name: 分类名称
  image_url: 分类图片
  created_at: 创建时间
  update_at: 更新时间
"""
class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.String(120), primary_key=True)
    category_name = db.Column(db.String(20), nullable=False, unique=True)
    image_url = db.Column(db.String(200), nullable=True)
    category_desc = db.Column(db.String(50), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False)
    update_at = db.Column(db.DateTime, server_default=db.func.now())

    def __repr__(self):
        return f"<products {self.username}>"