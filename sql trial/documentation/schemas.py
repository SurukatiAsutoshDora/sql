from pydantic import BaseModel
from datetime import datetime


class Item(BaseModel):
    item_id:int
    item_name: str
    item_price: int
    item_volume: int
    item_manufacture_date: datetime
    item_expiry_date: datetime
    item_shelf_number: str
    class Config:
        orm_mode=True