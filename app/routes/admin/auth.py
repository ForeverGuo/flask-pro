from flask import Blueprint
from app.models.admin import User
from app.utils.response import success_response, error_response
from app.utils.validator import validate_model
from app.routes.admin.schemas.authSchame import LoginModel
from flask_jwt_extended import create_access_token

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/login', methods=['POST'])
@validate_model(LoginModel)
def login(username, password):
    if not username or not password:
        return error_response('Invalid username or password', 400)
    
    # 查询用户
    user = User.query.filter_by(username=username).first()
    if not user:
        return error_response('用户不存在', 400)
    if not user.verify_password(password):
        return error_response('密码错误,请重新尝试', 400)

    return success_response({
      "user_id": user.user_id,
      "username": user.username,
      "avatar": user.avatar,
      "email": user.email,
      "phone": user.phone,
      "token": create_access_token(identity=user.user_id)
    })