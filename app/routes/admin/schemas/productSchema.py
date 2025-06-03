from typing import Optional
from pydantic import BaseModel

class productModel(BaseModel):
    id: Optional[str] = None
    product_name: str
    price: float
    product_desc: Optional[str] = None
    image_url: Optional[str] = None
    stock: int
    category_id: str
    status: Optional[int] = 0
    created_at: Optional[str] = None
    skus: Optional[list] = None

class productUpdateModel(BaseModel):
    id: str
    product_name: Optional[str] = None
    price: Optional[float] = None
    product_desc: Optional[str] = None
    image_url: Optional[str] = None
    stock: Optional[int] = None
    category_id: Optional[str] = None
    status: Optional[int] = 0

