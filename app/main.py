from fastapi import FastAPI
from .database import Base, engine
from .routes import user, listing

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user.router, prefix="/user", tags=["User"])
app.include_router(listing.router, prefix="/listing", tags=["Listing"])