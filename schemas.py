from pydantic import BaseModel

class CoursesCreate(BaseModel):
    id: int
    author: str
    title: str
    audience: int
    rating: float
    enrollment: bool
