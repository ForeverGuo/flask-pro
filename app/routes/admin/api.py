from flask import Blueprint
from flask_restx import Api

# 创建一个 Blueprint，它将包含所有的 API 命名空间
admin_api_bp = Blueprint('admin_api', __name__, url_prefix='/api/admin/v1')

# 在这个 Blueprint 上初始化 Flask-RESTx Api
# 注意: doc='/' 会在 /api/v1/doc/ 访问 Swagger UI
admin_api = Api(admin_api_bp,
          version='1.0',
          title='web管理后台API',
          description='web管理后台API',
          contact='Petter guo',
          doc='/doc/') # 对应 /api/v1/doc/

# 导入并注册所有的 API 命名空间到这个 api 实例
# 这样，所有在各个 routes.py 中定义的 namespace 都会被收集到这里
from app.routes.admin.user import user_bp

admin_api.add_namespace(user_bp)

