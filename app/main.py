from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)
app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/short_link/")
def get_or_create_short_link(link: schemas.LongLink, db: Session = Depends(get_db)):
    short_link = crud.get_or_create_short_link(link=link, db=db)
    return short_link
