from sqlalchemy.orm import Session
from . import models, schemas
import base64
from datetime import date, timedelta
from fastapi import HTTPException


def get_or_create_short_link(db: Session, link: schemas.LongLink):
    link_bd = (
        db.query(models.Link).filter(models.Link.long_link == link.long_link).first()
    )
    if link_bd is None:
        today = date.today()
        end_date = today + timedelta(days=int(link.expiration_date))
        end_one_year = today + timedelta(days=365)
        link = models.Link(
            long_link=link.long_link,
            end_date=end_date,
            end_one_year=end_one_year,
        )
        db.add(link)
        db.commit()

        link_bd = (
            db.query(models.Link)
            .filter(models.Link.long_link == link.long_link)
            .first()
        )
        id = link_bd.id
        short_link = base64.b64encode((str(id)).encode()).decode("utf-8").rstrip("=")

        link_bd.short_link = short_link
        db.add(link_bd)
        db.commit()
        db.refresh(link_bd)

    return link_bd


def redirect_long_link(db: Session, link):
    link_bd = db.query(models.Link).filter(models.Link.short_link == link).first()
    today = date.today()
    if (
        link_bd is not None
        and link_bd.end_date >= today
        and link_bd.end_one_year >= link_bd.end_one_year
    ):
        long_link = link_bd.long_link
        return long_link
    else:
        raise HTTPException(status_code=404, detail="Item not found")
