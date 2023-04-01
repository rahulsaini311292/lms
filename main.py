from fastapi import FastAPI
from lms.lib.database import SessionLocal, engine
from lms.handlers.root import root_router
from lms.handlers.book import book_router
from lms.schema import book_models

app = FastAPI()

book_models.Base.metadata.create_all(bind=engine)

app.include_router(root_router)
app.include_router(book_router)
