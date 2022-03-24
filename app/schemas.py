from pydantic import BaseModel


class LongLink(BaseModel):
    long_link: str
    expiration_date: str

    class Config:
        orm_mode = True


class ShortLink(BaseModel):
    short_link: str

    class Config:
        orm_mode = True
