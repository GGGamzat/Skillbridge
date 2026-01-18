from sqlalchemy import Column, Integer, String, Float, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()


class PriceTick(Base):
    __tablename__ = "price_ticks"

    id = Column(Integer, primary_key=True, index=True)
    ticker = Column(String, index=True, nullable=False)
    price = Column(Float, nullable=False)
    timestamp = Column(Integer, nullable=False, index=True)
    created_at = Column(DateTime, default=func.now())

    def __repr__(self):
        return f"<PriceTick(ticker={self.ticker}, price={self.price}, timestamp={self.timestamp})>"