from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import PriceTick


router = APIRouter()




def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




@router.get("/prices")
def get_all_prices(ticker: str = Query(...), db: Session = Depends(get_db)):
    return db.query(PriceTick).filter(PriceTick.ticker == ticker).all()




@router.get("/prices/latest")
def get_latest_price(ticker: str = Query(...), db: Session = Depends(get_db)):
    return (
        db.query(PriceTick)
        .filter(PriceTick.ticker == ticker)
        .order_by(PriceTick.timestamp.desc())
        .first()
    )




@router.get("/prices/by-date")
def get_price_by_date(
    ticker: str = Query(...),
    from_ts: int = Query(...),
    to_ts: int = Query(...),
    db: Session = Depends(get_db)
):
    return (
        db.query(PriceTick)
        .filter(
            PriceTick.ticker == ticker,
            PriceTick.timestamp >= from_ts,
            PriceTick.timestamp <= to_ts
        )
        .all()
    )