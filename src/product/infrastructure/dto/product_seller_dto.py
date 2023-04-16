from pydantic import BaseModel


class ProductSellerDTO(BaseModel):
    seller_email: str
