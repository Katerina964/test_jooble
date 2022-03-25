from pydantic import BaseModel
from typing import Optional


class LongLink(BaseModel):
    long_link: str
    expiration_date: Optional[str] = 90

    class Config:
        orm_mode = True


class ShortLink(BaseModel):
    short_link: str

    class Config:
        orm_mode = True
