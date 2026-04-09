from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, schemas, database, auth

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_listing(
    listing: schemas.ListingCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    new_listing = models.Listing(
        title=listing.title,
        description=listing.description,
        owner_id=current_user.id
    )
    db.add(new_listing)
    db.commit()
    return {"msg": "Listing created"}

@router.get("/")
def get_listings(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    return db.query(models.Listing).filter(
        models.Listing.owner_id == current_user.id
    ).all()