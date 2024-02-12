from sqlalchemy import Column, ForeignKey
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

class CourseStudent(Base):
    __tablename__ = 'CourseStudent'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text, nullable=False)
    n_course = Column(Integer)
    rating = Column(Integer)
    id_course = Column(Integer, ForeignKey("Courses.id"))
