from sqlalchemy.orm import Session

import models, schemas


def get_item_by_id(db: Session, item_id: int):
    return db.query(models.Item).filter(models.Item.item_id == item_id).first()


def get_all_items(db: Session):
    return db.query(models.Item).all()

def get_home_page(db: Session):
    return "Welcome to My Inventory"




def delete_item_by_id(db: Session, item_id: int):
    item = db.query(models.Item).get(item_id)
    if item:
        db.delete(item)
        db.commit()
        return True
    return False

def update_item_by_id(db: Session, item_id: int, updated_values: dict):
    item = db.query(models.Item).get(item_id)
    if item:
        for key, value in updated_values.items():
            setattr(item, key, value)
        db.commit()
        return True
    return False


def create_item(db: Session, item):
    db_item = models.Item(item_id=item.item_id,item_name=item.item_name,item_price=item.item_price,item_volume=item.item_volume,item_manufacture_date=item.item_manufacture_date,item_expiry_date=item.item_expiry_date,item_shelf_number=item.item_shelf_number)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

