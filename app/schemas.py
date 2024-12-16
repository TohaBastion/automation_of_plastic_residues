from pydantic import BaseModel

class OrderItem(BaseModel):
    model_id: int
    quantity: int
