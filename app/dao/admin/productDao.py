
from app import db
from app.models.admin import (Product, ProductSku)
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
  
  """
    根据skuId获取商品sku
  """
  def get_by_skuId(self, sku_id): 
    return ProductSku.query.get(sku_id)

  @global_db_exception_handler
  def create(self, data, skus):
    """
      创建商品
    """
    product = self.model(**data)
    db.session.add(product)
    db.session.flush()
    skus = [ProductSku(**sku, product_id=product.id) for sku in skus]
    db.session.add_all(skus)
    return success_response("product created")

  @global_db_exception_handler  
  def update(self, instance, data, skus):
    for key, value in data.items():
      setattr(instance, key, value)
    for sku in skus:
      skuIns = self.get_by_skuId(sku.get('id'))
      for key, value in sku.items():
        setattr(skuIns, key, value)
    return success_response("product update success!")
  
  @global_db_exception_handler
  def delete(self, instance):
    skuIns = ProductSku.query.filter_by(product_id=instance.id).all()
    if skuIns:
      for sku in skuIns:
        db.session.delete(sku)
    db.session.delete(instance)
    return success_response("product delete success!")

product_dao = ProductDao(Product)

