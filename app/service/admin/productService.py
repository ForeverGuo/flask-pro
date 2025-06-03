from datetime import datetime
from app.dao.admin.productDao import product_dao
from app.utils.method import getNowTime
from app.utils.response import error_response
from app.utils.snowFlakeId import get_unique_id

class ProductService():
   def __init__(self, product_dao):
      self.model = product_dao

   def create_product(self, data):
      new_product_name = data.get("product_name")
      new_product = self.model.get_by_name(new_product_name)
      if new_product:
          return error_response('product already exists!')
      skus = data.pop("skus")
      data["id"] = str(get_unique_id(1,1))
      data["created_at"] = getNowTime()

      for sku in skus:
          sku["id"] = str(get_unique_id(1,2))
          sku["created_at"] = getNowTime()

      return self.model.create(data, skus)
   
   def update_product(self, data):
      id = data.get('id')
      if not id:
          return error_response('id is required!')
      new_product = self.model.get_by_id(id)
      if not new_product:
          return error_response('product not found!')
      data["update_at"] = datetime.now()
      skus = data.pop('skus')
      if skus:
          for sku in skus:
              sku_id = sku.get('id')
              if not sku_id:
                 return error_response('sku_id is required!')
      args = {
        "instance": new_product,
        "data": data,
        "skus": skus
      }
      return self.model.update(**args)
   
   def delete_product(self, product_id):
      product = self.model.get_by_id(product_id)
      if not product:
          return error_response('product not found!')
      return self.model.delete(product)


# 实例化服务层对象(依赖注入)
productService = ProductService(product_dao)