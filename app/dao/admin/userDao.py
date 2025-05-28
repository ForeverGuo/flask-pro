from app import db
from app.models.admin import User
from app.utils import global_db_exception_handler
from app.utils.response import error_response, success_response


class UserDao():
  def __init__(self, model):
    self.model = model
  def get_all(self):
    return self.model.query.all()

  @global_db_exception_handler
  def create(self, data):
    user = self.model(**data)
    db.session.add(user)
    return success_response("user add success!")

  @global_db_exception_handler  
  def update(self, instance, data):
    for key, value in data.items():
      setattr(instance, key, value)
    return success_response("user update success!")
  
  @global_db_exception_handler
  def delete(self, instance):
    db.session.delete(instance)
    return success_response("user delete success!")
  
  def get_by_id(self, user_id):
    user = self.model.query.filter_by(user_id=user_id).first()
    if not user:
      return None
    return self.model.query.get(user.id)
  
  def get_by_name(self, username):
    user = self.model.query.filter_by(username=username).first()
    if not user:
      return None
    return user
  
  def get_by_email(self, email):
    user = self.model.query.filter_by(email=email).first()
    if not user:
      return None
    return user
  
  def get_by_phone(self, phone):
    user = self.model.query.filter_by(phone=phone).first()
    if not user:
      return None
    return user
  
user_dao = UserDao(User)
