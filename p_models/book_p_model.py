import datetime
from pydantic import BaseModel, Field


class BookPModel(BaseModel):
    book_name: str = Field(max_length=100)


