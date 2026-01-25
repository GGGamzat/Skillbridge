# DeriTrack

Проект представляет собой клиент для получения цен криптовалют с биржи Deribit. Каждую минуту система автоматически собирает цены BTC и ETH и сохраняет их в базу данных PostgreSQL.

# Design Decisions
1. Использование aiohttp для клиента Deribit
2. Celery для периодических задач
3. FastAPI как фреймворк для API
4. PostgreSQL как основная БД
5. Redis как брокер для Celery

# 🚀 Запуск проекта
+ Клонируйте репозиторий и перейдите в папку проекта
```
git clone https://github.com/GGGamzat/DeriTrack.git
cd DeriTrack
```

+ Создайте в корне проекта файл .env со своими данными
```
# Database
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=deribit_db
DATABASE_URL=postgresql://postgres:postgres@db:5432/deribit_db

# Celery
CELERY_BROKER_URL=redis://redis:6379/0
CELERY_RESULT_BACKEND=redis://redis:6379/0

# Deribit
DERIBIT_API_URL=https://www.deribit.com/api/v2/public
```

+ Соберите и запустите с помощью Docker
```
docker-compose up --build
```

+ Запуск тестов
```
docker-compose exec web python tests/test_api.py
```

# 📡 API Эндпоинты

1. Получить все сохраненные данные по валюте
```
curl "http://localhost:8000/api/v1/prices?ticker=BTC_USD"
```
```
curl "http://localhost:8000/api/v1/prices?ticker=ETH_USD&limit=10"
```

2. Получить последнюю цену валюты
```
curl "http://localhost:8000/api/v1/prices/latest?ticker=BTC_USD"
```

3. Получить цену валюты с фильтром по дате
```
curl "http://localhost:8000/api/v1/prices/filter?ticker=ETH_USD&start_date=1700000000&end_date=1701000000"
```