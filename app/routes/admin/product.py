"""
    @description: 商品模块
    @author: Petter guo
"""
from flask import request
from flask_restx import Resource, fields
from .api import admin_api as api
from app.routes.admin.schemas.productSchema import productModel, productUpdateModel
from app.utils import (
    validate_model,
    error_response,
  )

from app.service.admin.productService import productService

product_bp = api.namespace('product', description="商品管理")

product_add_model = product_bp.model('新增商品', {
    "product_name": fields.String(description="商品名称", required=True),
    "price": fields.Float(description="商品价格", required=True),
    "stock": fields.Integer(description="商品库存", required=True),
    "category_id": fields.String(description="商品分类id", required=True),
    "description": fields.String(description="商品描述"),
    "image_url": fields.String(description="商品图片地址"),
})

product_update_model = product_bp.model('修改商品', {
    "id": fields.String(description="商品ID", required=True),
})

product_delete_model = product_bp.model('删除商品', {
    "product_id": fields.String(description="商品id", required=True),
})

@product_bp.route('/add')
class ProductAdd(Resource):
    @api.doc(description="添加商品")
    @api.expect(product_add_model)
    @api.response(200, '成功')
    @api.response(400, '客户端错误')
    @api.response(500, '服务端错误')
    @validate_model(productModel)
    def post(self, **productargs):
        """
          # 添加商品
        """
        return productService.create_product(productargs)

@product_bp.route('/update')
class ProductUpdate(Resource):
    @api.doc(description="修改商品")
    @api.expect(product_update_model)
    @api.response(200, '成功')
    @api.response(400, '客户端错误')
    @api.response(500, '服务端错误')
    @validate_model(productModel)
    def post(self, **productargs):
        """
          # 修改商品
        """
        if not productargs.get('id'):
            return error_response("id不能为空")
        params_json = request.json
        return productService.update_product(params_json)

@product_bp.route('/<product_id>') 
class ProductDelete(Resource):
    @api.doc(description="删除商品")
    @api.expect(product_delete_model)
    @api.response(200, '成功')
    @api.response(400, '客户端错误')
    @api.response(500, '服务端错误')
    def delete(self, product_id):
        """
          # 删除商品
        """
        if not product_id:
            return error_response("无效商品id")
        return productService.delete_product(product_id)



