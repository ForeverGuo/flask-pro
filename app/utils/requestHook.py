"""
    请求钩子，用于拦截请求，验证token
    @author: petterguo
    @date: 2025/05/14
"""
from http.client import HTTPException
from flask import request
from flask_jwt_extended import verify_jwt_in_request
from flask_jwt_extended.exceptions import NoAuthorizationError
from .response import error_response
from app import create_app
from app.models.admin import User
from .registerBlueprint import registerBlueprint

app, jwt = create_app()

# 注册蓝图
registerBlueprint(app)

EXCLUDED_ENDPOINTS = {
    'auth.login',        # 登录路由的函数名
    'register',     # 如果有注册路由
    'public',       # 如果有公共路由
    'static',       # Flask 的静态文件端点通常是 'static'
}

RESTX_WHITELIST = ['/doc', '/api', '/swaggerui', '/static']

# 仍然需要这个回调来加载用户对象，即使是全局验证,
# 可以直接使用 current_user 和 get_jwt_identity()
@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"] # 'sub' 是默认存储身份的 claim
    # print(identity, "==================")
    user = User.query.filter_by(user_id=identity).first()
    return User.query.get(user.id)

# ==== 全局 JWT 验证 hook ====
@app.before_request
def jwt_before_request():
    print(request.path)
    if any(request.path.startswith(p) for p in RESTX_WHITELIST):
        return None 

    # 如果当前请求的端点在排除列表中，则跳过验证
    if request.endpoint in EXCLUDED_ENDPOINTS:
        return # 返回 None 或不返回任何东西，让请求继续处理

    # 对于不在排除列表中的端点，执行 JWT 验证
    # 如果 Token 无效或缺失，verify_jwt_in_request() 会抛出异常
    try:
        verify_jwt_in_request()
        # 如果验证成功，current_user 和 get_jwt_identity() 就可以在视图函数中使用了
    except Exception as e:
        if isinstance(e, HTTPException):
            #  return jsonify({"msg": str(e)}), e.code
            return error_response("登录失效, 请重新登录", 500)
        elif isinstance(e, NoAuthorizationError):
             return error_response("登录失效, 请重新登录", 500)

        # 处理其他可能的异常
        else:
             return error_response("登录失效, 请重新登录", 500)
        
