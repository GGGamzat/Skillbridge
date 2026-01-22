from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from app import schemas
from app.database import get_db
from app.crud import (
    get_all_prices_by_ticker,
    get_latest_price_by_ticker,
    get_prices_by_date_range
)

router = APIRouter()


@router.get("/prices", response_model=List[schemas.PriceDataResponse])
def get_all_prices(
        ticker: str = Query(..., description="Тикер валюты (например, BTC_USD)"),
        limit: int = Query(100, description="Лимит записей"),
        db: Session = Depends(get_db)
):
    prices = get_all_prices_by_ticker(db, ticker, limit)

    if not prices:
        raise HTTPException(status_code=404, detail="No data found for this ticker")

    return prices


@router.get("/prices/latest", response_model=schemas.PriceDataResponse)
def get_latest_price(
        ticker: str = Query(..., description="Тикер валюты (например, BTC_USD)"),
        db: Session = Depends(get_db)
):
    price = get_latest_price_by_ticker(db, ticker)

    if not price:
        raise HTTPException(status_code=404, detail="No data found for this ticker")

    return price


@router.get("/prices/filter", response_model=List[schemas.PriceDataResponse])
def get_prices_by_date(
        ticker: str = Query(..., description="Тикер валюты (например, BTC_USD)"),
        start_date: int = Query(..., description="Начальная дата в UNIX timestamp"),
        end_date: Optional[int] = Query(None, description="Конечная дата в UNIX timestamp"),
        db: Session = Depends(get_db)
):
    prices = get_prices_by_date_range(db, ticker, start_date, end_date)

    if not prices:
        raise HTTPException(status_code=404, detail="No data found for this ticker and date range")

    return prices