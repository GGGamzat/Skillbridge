from pydantic import BaseModel
from typing import List


class PriceDataBase(BaseModel):
    ticker: str
    price: float
    timestamp: int


class PriceDataCreate(PriceDataBase):
    pass


class PriceDataResponse(PriceDataBase):
    id: int

    class Config:
        from_attributes = True