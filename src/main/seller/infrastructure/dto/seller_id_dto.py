from pydantic import BaseModel


class SellerIdDTO(BaseModel):
    id: str
