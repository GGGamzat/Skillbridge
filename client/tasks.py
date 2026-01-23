from celery import Celery
from app.database import SessionLocal
from app import models
from app.config import settings
import asyncio
import logging

logger = logging.getLogger(__name__)

celery_app = Celery('tasks',
                    broker=settings.CELERY_BROKER_URL,
                    backend=settings.CELERY_RESULT_BACKEND)

celery_app.conf.update(
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
    broker_connection_retry_on_startup=True
)


@celery_app.task
def fetch_prices():
    from client.deribit_client import DeribitClient

    logger.info("Starting price fetch...")

    client = DeribitClient(use_testnet=False)

    async def get_prices():
        return await client.get_all_prices()

    loop = asyncio.get_event_loop()
    prices_data = loop.run_until_complete(get_prices())

    db = SessionLocal()
    saved = 0
    try:
        for price in prices_data:
            record = models.PriceData(
                ticker=price["ticker"],
                price=price["price"],
                timestamp=price["timestamp"]
            )
            db.add(record)
            saved += 1
            logger.info(f"Saved {price['ticker']}: ${price['price']:.2f}")

        db.commit()
        logger.info(f"Done. Saved {saved} records.")

    except Exception as e:
        db.rollback()
        logger.error(f"Error: {e}")
    finally:
        db.close()

    return {"saved": saved, "status": "success"}


celery_app.conf.beat_schedule = {
    'fetch-prices-minute': {
        'task': 'client.tasks.fetch_prices',
        'schedule': 60.0,
    },
}