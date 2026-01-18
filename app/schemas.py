from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime


class PriceTickBase(BaseModel):
    ticker: str
    price: float
    timestamp: int


class PriceTickCreate(PriceTickBase):
    pass


class PriceTick(PriceTickBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class PriceResponse(BaseModel):
    ticker: str
    price: float
    timestamp: int
    datetime: datetime


class AllPricesResponse(BaseModel):
    ticker: str
    count: int
    prices: List[PriceResponse]