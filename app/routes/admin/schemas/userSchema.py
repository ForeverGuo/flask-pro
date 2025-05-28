from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, Field, field_validator

class UserAddModel(BaseModel):
    """
      新增用户模型
      Attributes:
        username (str): 用户名，长度在2到10之间
        password (str): 密码，长度在6到20之间
        email (EmailStr): 有效的邮箱地址
        phone (Optional[str]): 手机号码，可为空
        avatar (Optional[str]): 头像URL或路径，可为空
        user_id (Optional[str]): 用户唯一标识，默认为UUID生成
    """
    username: str = Field(min_length=2, max_length=10)
    password: str = Field(min_length=6, max_length=20)
    email: EmailStr
    phone: Optional[str] = None
    avatar: Optional[str] = None
    created_at: Optional[datetime] = datetime.now()
 
class UserUpdateModel(BaseModel):
    """
    更新用户模型
    """
    user_id: str
    @field_validator("user_id")
    def validate_userid(cls, v):
        if v is not None and len(v.strip()) == 0:
            raise ValueError("user_id cannot be empty")
        return v
    
class UserDeleteModel(BaseModel):
    """"
    删除用户模型
    """
    user_id: str

class UserListModel(BaseModel):
    """"
    用户列表模型
    """
    username: Optional[str] = None
    pageIndex: int = Field(default=1)
    pageSize: int = Field(default=10)