import datetime
from sqlalchemy import BOOLEAN, Column, Integer, VARCHAR, TIMESTAMP
from sqlalchemy.orm import relationship

from lms.lib.database import Base


class Book(Base):
    __tablename__ = "book"

    id = Column(Integer, primary_key=True, autoincrement=True)
    book_name = Column(VARCHAR(100), nullable=False, unique=True,)
    created_date = Column(TIMESTAMP, default=datetime.datetime.now())
    modified_date = Column(TIMESTAMP, default=None)
