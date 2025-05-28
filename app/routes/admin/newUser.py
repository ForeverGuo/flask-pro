# from flask import Blueprint
# from flask_restx import Resource, fields
# from app.routes.admin.service.userService import user_service
# from flask_restx import Api

# newuser = Blueprint('newuser', __name__, url_prefix='/newuser')


# flask_api = Api(
#     newuser,
#     version='1.0',
#     title='Flask API',
#     description='A simple Flask API',
#     doc='/doc/' 
# )

# user_ns = flask_api.namespace('newuser', description='用户管理')


# user_model = user_ns.model('User', {
#     'username': fields.String(description='用户名'),
#     'email': fields.String(description='用户邮箱')
# })

# @user_ns.route('/')
# class UserListResource(Resource):
#   @user_ns.doc(description='获取所有用户')
#   @user_ns.marshal_list_with(user_model)
#   @user_ns.response(200, '获取所有用户成功')
#   def get(self):
#     users = user_service.get_all_users()
#     return users