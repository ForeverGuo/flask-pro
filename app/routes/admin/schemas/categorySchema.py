from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, field_validator

class categoryAddModel(BaseModel):
    category_name: str
    category_desc: Optional[str] = None
    image_url: Optional[str] = None
    created_at: Optional[datetime] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class categoryUpdateModel(BaseModel):
    id: str
    @field_validator("id")
    def validate_categoryid(cls, v):
        if not v:
            raise ValueError('id is required')
        return v
