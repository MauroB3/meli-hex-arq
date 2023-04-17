from pydantic import BaseModel


class PurchaseProductIdDTO(BaseModel):
    product_id: str
