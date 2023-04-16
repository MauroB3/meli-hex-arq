from pydantic import BaseModel


class ProductNameSellerDTO(BaseModel):
    seller_email: str
    name: str
