"""
    @description: 商品模块
    @author: Petter guo
"""
from flask import Blueprint
from app.routes.admin.schemas.productSchema import productModel, productUpdateModel
from app.utils import (
    validate_model,
    error_response,
  )

from app.service.admin.productService import productService

product_bp = Blueprint('product', __name__, url_prefix='/product')

"""
    @description: 添加商品
    @param product_name: 商品名称
    @param price: 商品价格
    @param description: 商品描述
    @param image_url: 商品图片地址
    @author: Petter guo
"""
@product_bp.route('/add', methods=['POST'])
@validate_model(productModel)
def add_product(**productargs):
    return productService.create_product(productargs)

"""
    @description: 修改商品
    @param product_id: 商品id
    @author: Petter guo
"""
@product_bp.route("/update", methods = ["POST"])
@validate_model(productUpdateModel)
def update_product(**productargs):
    return productService.update_product(productargs)

"""
    @description: 删除商品
    @param product_id: 商品id
    @author Petter guo
    @return: 删除成功
"""
@product_bp.route('/<product_id>', methods=['DELETE'])
def delete_product(product_id):
    if not product_id:
        return error_response('Invalid product id')
    return productService.delete_product(product_id)


