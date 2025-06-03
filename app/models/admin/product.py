from app import db

"""
  商品列表
  id: 商品id
  name: 商品名称
  price: 商品价格
  description: 商品描述
  image_url: 商品图片地址
  stock: 商品库存
  status: 商品状态
  category_id: 商品分类id(外键关联)
  created_at: 创建时间
  updated_at: 更新时间
"""
class Product (db.Model):
    __tablename__ = 'products'

    id = db.Column(db.String(120), primary_key=True)
    product_name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    product_desc = db.Column(db.String(200), nullable=True)
    image_url = db.Column(db.String(200), nullable=True)
    stock = db.Column(db.Integer, nullable=True)
    # 状态 0 - 下架 1 - 上架
    status = db.Column(db.Integer, nullable=True, default=0)
    # 分类id
    category_id = db.Column(db.String(300), db.ForeignKey('categories.id'), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    update_at = db.Column(db.DateTime, server_default=db.func.now())
    skus = db.relationship("ProductSku", backref="product", lazy=True)

    def __repr__(self):
        return f"<products {self.username}>"



"""
  商品sku表
  id: sku id
  product_id: 商品id
  sku_name: sku名称
  price: sku价格
  stock: sku库存
  image_url: 图片url
  created_at: 创建时间
  update_at: 更新时间
"""
class ProductSku(db.Model):
    __tablename__ = 'product_skus'

    id = db.Column(db.String(120), primary_key=True)
    product_id = db.Column(db.String(120), db.ForeignKey('products.id'), nullable=False)
    attributes = db.Column(db.JSON, nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, server_default=db.func.now())

    def __repr__(self):
        return f"<product_skus {self.product_id}>"