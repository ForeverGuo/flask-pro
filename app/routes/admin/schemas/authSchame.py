from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, Field, field_validator

class LoginModel(BaseModel):
    username: str
    password: str