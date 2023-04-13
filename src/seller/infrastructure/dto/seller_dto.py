from pydantic import BaseModel


class SellerDTO(BaseModel):
    name: str
    email: str
