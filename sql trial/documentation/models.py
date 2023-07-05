from sqlalchemy import Column,Integer, String, DateTime

from database import Base


class Item(Base):
    __tablename__ = "TRIAL10"

    item_id = Column(Integer, primary_key=True)
    item_name = Column(String)
    item_price = Column(Integer)
    item_volume= Column(Integer)
    item_manufacture_date=Column(DateTime)
    item_expiry_date=Column(DateTime)
    item_shelf_number=Column(String)



