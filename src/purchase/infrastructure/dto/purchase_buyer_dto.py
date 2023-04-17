from pydantic import BaseModel


class PurchaseBuyerDTO(BaseModel):
    buyer_email: str
