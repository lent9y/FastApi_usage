import asyncio
import typer
from fastapi import FastAPI
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel
from sqlalchemy.exc import IntegrityError
#import DuplicatedEntryError
from base import init_models
from base import get_session
import service

cli = typer.Typer()
app = FastAPI()

class CoursesCreate(BaseModel):
    id: int
    author: str
    title: str
    audience: int
    rating: float
    enrollment: bool

@cli.command()
def db_init_models():
    asyncio.run(init_models())
    print("Done")


if __name__ == "__main__":
    cli()

@app.get("/courses/best", response_model=list[CoursesCreate])
async def get_best_courses(session: AsyncSession = Depends(get_session)):
    courses = await service.get_best_courses(session)
    return [CoursesCreate(id=c.id, author=c.author, title=c.title, audience=c.audience, rating=c.rating, enrollment=c.enrollment) for c in courses]


@app.post("/courses/")
async def add_course(course: CoursesCreate, session: AsyncSession = Depends(get_session)):
    course = service.add_course(session, course.id, course.author, course.title, course.audience, course.rating, course.enrollment)
    #try:
    await session.commit()
    return course
    # except IntegrityError as ex:
    #     await session.rollback()
    #     raise DuplicatedEntryError("The city is already stored")