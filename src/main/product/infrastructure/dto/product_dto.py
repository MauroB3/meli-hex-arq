from pydantic import BaseModel


class ProductDTO(BaseModel):
    seller_email: str
    name: str
    description: str
    price: float
    stock: int = 0
