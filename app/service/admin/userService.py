from datetime import datetime
from app.dao.admin.userDao import user_dao
from app.utils.response import error_response
from app.utils.snowFlakeId import get_unique_id
from werkzeug.security import generate_password_hash, check_password_hash

class UserService():
  def __init__(self, user_dao):
    self.user_dao = user_dao

  def get_all_users(self):
        return self.user_dao.get_all()
  
  def get_user_by_id(self, user_id):
    return self.user_dao.get_by_id(user_id)
  
  def create_user(self, data):
     email = data['email']
     phone = data['phone']
     user = data['username']
     user = user if self.user_dao.get_by_name(user) else None
     if user:
       return error_response("用户名已存在")
     email = email if self.user_dao.get_by_email(email) else None
     if email:
       return error_response("邮箱已存在")
     phone = phone if self.user_dao.get_by_phone(phone) else None
     if phone:
       return error_response("手机号已存在")
     data["password_hash"] = self.set_password(data['password'])
     data['user_id'] = get_unique_id()
     return self.user_dao.create(data)
  
  def delete_user(self, user_id):
    user = self.get_user_by_id(user_id)
    if not user:
      return error_response("User not found")
    return self.user_dao.delete(user)
  
  def update_user(self, data):
    password = data.get('password') or None
    user_id = data.get('user_id')
    user = self.get_user_by_id(user_id)
    if not user:
      return error_response('user not found!')
    if password:
      data['password_hash'] = self.set_password(password)
    data["update_at"] = datetime.now()
    return self.user_dao.update(user, data)
 
  def set_password(self, password):
    return generate_password_hash(
            password, 
            method='pbkdf2:sha256:10000',  # 格式：算法:哈希方法:迭代次数
            salt_length=16
        )
  
  def verify_password(self, password_hash, password):
      return check_password_hash(password_hash, password)
  
  def get_users_by_page(self, data):
    username = data.get('username', '')
    pageIndex = data.get('pageIndex', 1)
    pageSize = data.get('pageSize', 10)
    userDao = self.user_dao.model
    list = userDao.query.filter(userDao.username.like(f"%{username}%"))

    data = list.paginate(page=pageIndex, per_page=pageSize, error_out=False)
    lists = [dict(
        username=user.username, 
        email=user.email,
        avatar = user.avatar,
        phone = user.phone,
        user_id = user.user_id,
      ) for user in data.items]
    return {
      "list": lists or  [],
      "total": data.total,
      "pageIndex": data.page,
      "pageSize": data.per_page,
    }

  
# 实例化服务层对象(依赖注入)
userService = UserService(user_dao)
