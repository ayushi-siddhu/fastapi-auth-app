from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, schemas, database

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_listing(listing: schemas.ListingCreate, db: Session = Depends(get_db)):
    new_listing = models.Listing(**listing.dict(), owner_id=1)
    db.add(new_listing)
    db.commit()
    return {"msg": "Listing created"}

@router.get("/")
def get_listings(db: Session = Depends(get_db)):
    return db.query(models.Listing).all()