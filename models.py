from sqlalchemy import Column
from sqlalchemy import Integer, Text, Float, Boolean
from base import Base

class Courses(Base):
    __tablename__ = 'Courses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    author = Column(Text, nullable=False)
    title = Column(Text, nullable=False)
    audience = Column(Integer)
    rating = Column(Float, nullable=False)
    enrollment = Column(Boolean)
