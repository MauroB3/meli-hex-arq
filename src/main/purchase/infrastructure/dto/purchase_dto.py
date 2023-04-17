from pydantic import BaseModel


class PurchaseDTO(BaseModel):
    product_id: str
    buyer_email: str
    amount: int
