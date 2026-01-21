from sqlalchemy import Column, Integer, String, Float, BigInteger
from app.database import Base


class PriceData(Base):
    __tablename__ = "price_data"

    id = Column(Integer, primary_key=True, index=True)
    ticker = Column(String, index=True, nullable=False)
    price = Column(Float, nullable=False)
    timestamp = Column(BigInteger, nullable=False)

    def __repr__(self):
        return f"<PriceData {self.ticker}: {self.price} at {self.timestamp}>"