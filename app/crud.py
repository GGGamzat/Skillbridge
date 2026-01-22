from sqlalchemy.orm import Session
from typing import List, Optional
from app import models


def get_all_prices_by_ticker(db: Session, ticker: str, limit: int = 100) -> List[models.PriceData]:
    return db.query(models.PriceData) \
        .filter(models.PriceData.ticker == ticker.upper()) \
        .order_by(models.PriceData.timestamp.desc()) \
        .limit(limit) \
        .all()


def get_latest_price_by_ticker(db: Session, ticker: str) -> Optional[models.PriceData]:
    return db.query(models.PriceData) \
        .filter(models.PriceData.ticker == ticker.upper()) \
        .order_by(models.PriceData.timestamp.desc()) \
        .first()


def get_prices_by_date_range(
        db: Session,
        ticker: str,
        start_timestamp: int,
        end_timestamp: Optional[int] = None
) -> List[models.PriceData]:
    query = db.query(models.PriceData) \
        .filter(models.PriceData.ticker == ticker.upper()) \
        .filter(models.PriceData.timestamp >= start_timestamp)

    if end_timestamp:
        query = query.filter(models.PriceData.timestamp <= end_timestamp)

    return query.order_by(models.PriceData.timestamp.asc()).all()