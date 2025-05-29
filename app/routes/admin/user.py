"""
  title: 用户管理
  author: petter
  date: 2025/05/13
"""
from flask import request
from flask_restx import Resource, fields
from .api import admin_api as api

from app.routes.admin.schemas.userSchema import (
    UserAddModel, 
    UserUpdateModel,
    UserListModel
)
from app.utils import validate_model, success_response, error_response

from app.service.admin.userService import userService

user_bp = api.namespace('user', description="用户管理")

user_add_model = user_bp.model('添加用户', {
    "username": fields.String(description="用户名", required=True),
    "password": fields.String(description="密码", required=True),
    "phone": fields.String(description="手机号"),
    "email": fields.String(description="邮箱", required=True),
    "avatar": fields.String(description="头像"),
})

user_update_model = user_bp.model('修改用户', {
    "user_id": fields.String(description="用户id", required=True),
    "username": fields.String(description="用户名"),
    "password": fields.String(description="密码"),
    "phone": fields.String(description="手机号"),
    "email": fields.String(description="邮箱"),
    "avatar": fields.String(description="头像"),
})

user_list_model = user_bp.model('用户列表', {
    "pageIndex": fields.Integer(description="分页码", required=True, default=1),
    "pageSize": fields.String(description="数据条数", required=True, default=10),
    "username": fields.String(description="用户名"),
})

user_delete_model = user_bp.model('删除用户', {
    "user_id": fields.String(description="用户id", required=True),
})

@user_bp.route('/add', methods=['POST'])
class UserAdd(Resource):
    @api.doc(description='新增用户')
    @api.expect(user_add_model)
    @api.response(200, '成功')
    @api.response(400, '客户端错误')
    @api.response(500, '服务端错误')
    @validate_model(UserAddModel)
    def post(self, **userargs):
        """
          # 新增用户
        """
        return userService.create_user(userargs)


@user_bp.route('/update', methods=['POST'])
class UserUpdate(Resource):
    @api.doc(description='更新用户')
    @api.expect(user_update_model)
    @api.response(200, '成功')
    @api.response(400, '客户端错误')
    @api.response(500, '服务端错误')
    @validate_model(UserUpdateModel)
    def post(self, **userargs):
        """
          # 更新用户
        """
        user_id = userargs.get('user_id')
        if not user_id:
            return error_response('user_id is required')
        user_json = request.json
        return userService.update_user(user_json) 

@user_bp.route('/<user_id>')
class UserDelete(Resource):
    @api.doc(description='删除用户')
    @api.expect(user_delete_model)
    @api.response(200, '成功')
    @api.response(400, '客户端错误')
    @api.response(500, '服务端错误')
    def delete(self, user_id):
        """
          # 删除用户
        """
        if not user_id:
            return error_response('user_id is required')
        return userService.delete_user(user_id), 200


@user_bp.route('/list')
class UserList(Resource):
    @api.doc(description='获取所有用户')
    @api.expect(user_list_model)
    @api.response(200, '成功')
    @api.response(400, '客户端错误')
    @api.response(500, '服务端错误')
    @validate_model(UserListModel)
    def post(self, **dataargs):
      """
        # 获取所有用户
      """
      res = userService.get_users_by_page(dataargs)
      return success_response(res)

