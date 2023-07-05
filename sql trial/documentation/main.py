from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/new-item")
def create_user(item_id:int ,item:schemas.Item, db: Session = Depends(get_db)):
    db_item = crud.get_item_by_id(db, item_id)
    if db_item:
        
        raise HTTPException(status_code=400, detail="ID is already present")
    return crud.create_item(db=db, item=item)

@app.get("/")
def get_welcome_page(db:Session=Depends(get_db)):
     items=crud.get_home_page(db)
     return items



@app.get("/items")
def get_items( db: Session = Depends(get_db)):
    items = crud.get_all_items(db)
    return items


@app.put("/update-item/{item_id}")
def update_item(item_id: int, updated_item: schemas.Item, db: Session = Depends(get_db)):
    existing_item = crud.get_item_by_id(db, item_id)
    if existing_item:
        updated_values = updated_item.dict(exclude_unset=True)
        crud.update_item_by_id(db, item_id=item_id, updated_values=updated_values)
        return {"message": "Item updated successfully"}
    raise HTTPException(status_code=404, detail="Item not found")


@app.delete("/delete-item/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    item = crud.get_item_by_id(db, item_id) 
    if item:
        crud.delete_item_by_id(db, item_id) 
        return {"message": "Item deleted successfully"}
    raise HTTPException(status_code=404, detail="No Item is present with this ID")







