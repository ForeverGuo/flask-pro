"""
  @description: 分类管理
  @author: Petter guo
"""
from flask import request
from flask_restx import Resource, fields
from .api import admin_api as api
from app.routes.admin.schemas.categorySchema import categoryAddModel, categoryUpdateModel
from app.utils import (
    validate_model,
    error_response
)

from app.service.admin.categoryService import categoryService

category_bp = api.namespace('category', description="分类管理")

category_add_model = api.model('新增分类', {
    'category_name': fields.String(required=True, description='分类名称'),
    'image_url': fields.String(description='分类图片地址'),
    'category_desc': fields.String(description='分类描述'),
})

category_update_model = api.model('修改分类', {
    'id': fields.String(required=True, description='分类id')
})

category_delete_model = api.model('删除分类', {
    'id': fields.String(required=True, description='分类id')
})

@category_bp.route('/add')
class CategoryAdd(Resource):
    @api.doc(description="添加分类")
    @api.expect(category_add_model)
    @api.response(200, '成功')
    @api.response(400, '客户端错误')
    @api.response(500, '服务端错误')
    @validate_model(categoryAddModel)
    def post(self, **categoryargs):
        """
        # 添加分类
        """
        return categoryService.create_category(categoryargs)

@category_bp.route('/update')
class CategoryUpdate(Resource):
    @api.doc(description="修改分类")
    @api.expect(category_update_model)
    @api.response(200, '成功')
    @api.response(400, '客户端错误')
    @api.response(500, '服务端错误')
    @validate_model(categoryUpdateModel)
    def post(self, **categoryargs):
        """
        # 修改分类
        """
        if not categoryargs.get('id'):
            return error_response("id不能为空")
        params_json = request.json
        return categoryService.update_category(params_json)

@category_bp.route('/<category_id>')
class CategoryDelete(Resource):
    @api.doc(description="删除分类")
    @api.expect(category_delete_model)
    @api.response(200, '成功')
    @api.response(400, '客户端错误')
    @api.response(500, '服务端错误')
    def delete(self, category_id):
        """
        # 删除分类
        """
        if not category_id:
          return error_response("id不能为空")
        return categoryService.delete_category(category_id)
