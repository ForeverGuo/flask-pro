
from app import db
from app.models.admin import Product
from app.utils import global_db_exception_handler
from app.utils.response import success_response

class ProductDao():
  def __init__(self, model):
    self.model = model

  
  def get_by_id(self, product_id):
    """
      根据商品id获取商品
    """
    product = self.model.query.filter_by(id=product_id).first()
    if not product:
      return None
    return self.model.query.get(product_id)
  
  def get_by_name(self, product_name):
    """
      根据商品名称获取商品
    """
    product = self.model.query.filter_by(product_name=product_name).first()
    return product
  
  def get_all(self):
    """
      获取所有商品
    """
    products = self.model.query.all()
    return products

  @global_db_exception_handler
  def create(self, data):
    """
      创建商品
    """
    product = self.model(**data)
    db.session.add(product)
    return success_response("product created")

  @global_db_exception_handler  
  def update(self, instance, data):
    for key, value in data.items():
      setattr(instance, key, value)
    return success_response("product update success!")
  
  @global_db_exception_handler
  def delete(self, instance):
    db.session.delete(instance)
    return success_response("product delete success!")

product_dao = ProductDao(Product)

