"""
  @description: 分类管理
  @author: Petter guo
"""
from flask import Blueprint, request
from app.routes.admin.schemas.categorySchema import categoryAddModel, categoryUpdateModel
from app.utils import (
    validate_model,
    error_response
)

from app.service.admin.categoryService import categoryService

category_bp = Blueprint('category', __name__, url_prefix='/category')

@category_bp.route('/add', methods=['POST'])
@validate_model(categoryAddModel)
def add_category(**categoryargs):
    """
        添加分类
        @param category_name: 分类名称
        @param image_url: 分类图片地址
        @param category_desc: 分类描述
        @param created_at: 创建时间
        @return:
    """
    return categoryService.create_category(categoryargs)

@category_bp.route("/update", methods=["POST"])
@validate_model(categoryUpdateModel)
def update_category(**categoryargs):
    """
      修改分类
    """
    if not categoryargs.get('id'):
        return error_response("id不能为空")
    params_json = request.json
    return categoryService.update_category(params_json)

@category_bp.route('/<category_id>', methods=['DELETE'])
def delete_category(category_id):
    """
        删除分类
        @param category_id: 分类id
    """
    if not category_id:
        return error_response("id不能为空")
    return categoryService.delete_category(category_id)