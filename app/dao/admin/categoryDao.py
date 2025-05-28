from app.models.admin import Category
from app.utils import (
  global_db_exception_handler,
  success_response,
  error_response
)
from app import db

class CategoryDao():
  def __init__(self, model):
    self.model = model

  def get_all(self):
    """
      @description: 获取所有分类
      @author: Petter guo
      @param {*}
      @return: 
    """
    categories = self.model.query.all()
    return success_response(categories)

  @global_db_exception_handler
  def create(self, data):
    """
      @description: 创建分类
      @author: Petter guo
      @param {*}
      @return: 
    """
    category = self.model(**data)
    db.session.add(category)
    return success_response("category created successfully!")
  @global_db_exception_handler
  def update(self, instance, data):
    """
      @description: 更新分类
      @author: Petter guo
      @param {*}
      @return: 
    """
    for key, value in data.items():
      setattr(instance, key, value)
    return success_response("category updated successfully!")
  @global_db_exception_handler
  def delete(self, instance):
    """
      @description: 删除分类
      @author: Petter guo
      @param {*}
      @return: 
    """
    db.session.delete(instance)
    return success_response("category deleted successfully!")
  
  def get_by_id(self, category_id):
    """
      @description: 根据id查询分类
      @author: Petter guo
      @param {*}
      @return: 
    """
    category = self.model.query.filter_by(id = category_id).first()
    if not category:
      return error_response("category not found!")
    return Category.query.get(category_id)
  
  def get_by_name(self, category_name):
    """
      @description: 根据name查询分类
      @author: Petter guo
      @param {*}
      @return: 
    """
    category = self.model.query.filter_by(category_name = category_name).first()
    if not category:
      return None
    return Category.query.filter_by(category_name= category_name).first()


category_dao = CategoryDao(Category)