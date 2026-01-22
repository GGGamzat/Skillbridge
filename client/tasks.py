from celery import Celery
from client.deribit_client import DeribitClient
from app.database import SessionLocal
from app import models
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


@celery_app.task
def fetch_and_store_prices():
    client = DeribitClient()

    async def fetch_prices():
        return await client.get_prices(["btc", "eth"])

    loop = asyncio.get_event_loop()
    prices_data = loop.run_until_complete(fetch_prices())

    db = SessionLocal()
    try:
        for price_item in prices_data:
            price_record = models.PriceData(
                ticker=price_item["ticker"],
                price=price_item["price"],
                timestamp=price_item["timestamp"]
            )
            db.add(price_record)
        db.commit()
        logger.info(f"Сохранено {len(prices_data)} записей")
    except Exception as e:
        db.rollback()
        logger.error(f"Ошибка сохранения в БД: {e}")
    finally:
        db.close()

    return {"status": "success", "records_saved": len(prices_data)}


celery_app.conf.beat_schedule = {
    'fetch-prices-every-minute': {
        'task': 'client.tasks.fetch_and_store_prices',
        'schedule': 60.0,
    },
}