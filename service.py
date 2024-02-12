from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models import *


async def get_best_courses(session: AsyncSession) -> list[Courses]:
    result = await session.execute(select(Courses).order_by(Courses.rating.desc()).limit(20))
    return result.scalars().all()


def add_course(session: AsyncSession, id: int, author: str, title: str, audience: int, rating: float, enrollment: bool):
    new_course = Courses(id=id, author=author, title=title, audience=audience, rating=rating, enrollment=enrollment)
    session.add(new_course)
    return new_course
