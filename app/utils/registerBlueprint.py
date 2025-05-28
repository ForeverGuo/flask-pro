from app.routes.admin.api import admin_api_bp, admin_api
from app.routes import (
   auth_bp, 
   home_bp, 
   category_bp,
   upload_bp,
   user_bp,
   product_bp
)
def registerBlueprint(app):
    """
    title: 注册蓝图
    """
    app.register_blueprint(admin_api_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(home_bp)
    app.register_blueprint(category_bp)
    app.register_blueprint(upload_bp)
    admin_api.add_namespace(user_bp)
    admin_api.add_namespace(product_bp)
