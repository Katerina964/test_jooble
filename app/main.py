from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine
from fastapi.responses import RedirectResponse

models.Base.metadata.create_all(bind=engine)
app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/short_link/", response_model=schemas.ShortLink)
def get_or_create_short_link(link: schemas.LongLink, db: Session = Depends(get_db)):
    short_link = crud.get_or_create_short_link(link=link, db=db)
    return short_link


@app.get("/link/{link}/", response_class=RedirectResponse)
def redirect_long_link(link: str, db: Session = Depends(get_db)):
    url = crud.redirect_long_link(link=link, db=db)
    return url
