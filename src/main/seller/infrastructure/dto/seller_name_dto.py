from pydantic import BaseModel


class SellerNameDTO(BaseModel):
    name: str
