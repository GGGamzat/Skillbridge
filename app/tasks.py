from celery import Celery
from app.deribit_client import DeribitClient
from app.database import SessionLocal
from app.models import PriceData
from app.config import settings
import asyncio
import logging

logger = logging.getLogger(__name__)

celery_app = Celery(
    'tasks',
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_RESULT_BACKEND
)

celery_app.conf.update(
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
)


def run_async(coro):
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(coro)


@celery_app.task
def fetch_and_store_prices():
    client = DeribitClient()

    prices = run_async(client.get_prices(["btc", "eth"]))

    db = SessionLocal()
    try:
        for price_data in prices:
            price_record = PriceData(
                ticker=price_data["ticker"],
                price=price_data["price"],
                timestamp=price_data["timestamp"]
            )
            db.add(price_record)
        db.commit()
        logger.info(f"Saved {len(prices)} price records")
    except Exception as e:
        db.rollback()
        logger.error(f"Error saving to database: {e}")
    finally:
        db.close()

    return {"status": "success", "records_saved": len(prices)}


celery_app.conf.beat_schedule = {
    'fetch-prices-every-minute': {
        'task': 'client.tasks.fetch_and_store_prices',
        'schedule': 60.0,
    },
}