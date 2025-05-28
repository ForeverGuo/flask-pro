"""
    @description: 商品模块
    @author: Petter guo
"""
from flask_restx import Resource, fields
from .api import admin_api as product_api
from app.routes.admin.schemas.productSchema import productModel, productUpdateModel
from app.utils import (
    validate_model,
    error_response,
  )

from app.service.admin.productService import productService

product_bp = product_api.namespace('product', description="商品管理")

product_add_model = product_bp.model('add_product_params', {
    "product_name": fields.String(description="商品名称", required=True),
    "price": fields.Float(description="商品价格", required=True),
    "stock": fields.Integer(description="商品库存", required=True),
    "category_id": fields.String(description="商品分类id", required=True),
    "description": fields.String(description="商品描述"),
    "image_url": fields.String(description="商品图片地址"),
})

@product_bp.route('/add')
class ProductAdd(Resource):
    @product_api.doc(description="添加商品")
    @product_api.expect(product_add_model)
    @product_api.response(200, '成功')
    @product_api.response(400, '客户端错误')
    @product_api.response(500, '服务端错误')
    @validate_model(productModel)
    def post(self, **productargs):
        """
          # 添加商品
        """
        return productService.create_product(productargs)
    

# @product_bp.route('/add', methods=['POST'])
# @validate_model(productModel)
# def add_product(**productargs):
#     return productService.create_product(productargs)

"""
    @description: 修改商品
    @param product_id: 商品id
    @author: Petter guo
"""
# @product_bp.route("/update", methods = ["POST"])
# @validate_model(productUpdateModel)
# def update_product(**productargs):
#     return productService.update_product(productargs)

# """
#     @description: 删除商品
#     @param product_id: 商品id
#     @author Petter guo
#     @return: 删除成功
# """
# @product_bp.route('/<product_id>', methods=['DELETE'])
# def delete_product(product_id):
#     if not product_id:
#         return error_response('Invalid product id')
#     return productService.delete_product(product_id)


