from fastapi import FastAPI
from app.routes import router
from app.database import engine
from app import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Deribit Price API",
    description="API для получения цен криптовалют с Deribit",
    version="1.0.0"
)

app.include_router(router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Deribit Price API", "status": "running"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}