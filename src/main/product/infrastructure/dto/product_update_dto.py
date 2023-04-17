from pydantic import BaseModel


class ProductUpdateDTO(BaseModel):
    id: str
    name: str
    description: str
    price: float
    category: str
    stock: int
