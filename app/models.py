from sqlalchemy import Column, String, Integer, Date
import datetime
from .database import Base


class Link(Base):
    __tablename__ = "links"

    id = Column(Integer, primary_key=True, index=True)
    long_link = Column(String, unique=True, index=True)
    short_link = Column(String, index=True, default="emty")
    expiration_date = Column(Integer, default=90)
    end_one_year = Column(Date, default=datetime.date.today)
