from fastapi import FastAPI
from app.core.config import settings
from sqlalchemy import text
from app.core.database.database_connection import engine

from app.api import test_route, book_route
from app.models.book import Base

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description=settings.APP_DESCRIPTION
)

app.include_router(test_route.router, prefix='/test', tags=['Test'])
app.include_router(book_route.router, prefix="/books", tags=["Books"])

@app.get("/health/db", tags=["Health"])
def check_database():
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
    return {"message": "Conexión a la base de datos exitosa"}
