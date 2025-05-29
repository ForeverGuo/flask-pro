from app.dao.admin.categoryDao import category_dao
from app.utils import (
  success_response,
  error_response
)
from app.utils.snowFlakeId import get_unique_id

class CatefgoryService():
  def __init__(self, category_dao):
    self.model = category_dao

  def create_category(self, data):
    """
        添加分类
        @param data: 分类信息
        @return:
    """
    category = self.model.get_by_name(data['category_name'])
    if category:
        return error_response('category_name already exists!')
    data["id"] = str(get_unique_id())
    return self.model.create(data)
  
  def update_category(self, data):
    """
        修改分类
        @param data: 分类信息
        @return:
    """
    id = data.get('id')
    curr_item = self.model.get_by_id(id)
    if not curr_item:
        return error_response('category not found!')
    name = data.get('category_name')
    if name and self.model.get_by_name(name):
        return error_response('category_name already exists!')
    return self.model.update(curr_item, data)
  
  def delete_category(self, category_id):
    """
        删除分类
        @param category_id: 分类id
    """
    category = self.model.get_by_id(category_id)
    if not category:
        return error_response('category not found!')
    return self.model.delete(category)



categoryService = CatefgoryService(category_dao)