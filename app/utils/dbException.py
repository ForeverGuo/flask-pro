from sqlalchemy.exc import SQLAlchemyError
from functools import wraps
from app.utils.response import error_response
from app import db
def global_db_exception_handler(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        try:
            result = func(self, *args, **kwargs)
            db.session.commit()
            return result
        except Exception as e:
            db.session.rollback()
            return error_response(f"数据库操作异常: {str(e)}")
        finally:
            db.session.close()
    return wrapper

