from pydantic import BaseModel, ConfigDict

class BookCreate(BaseModel):
    title: str
    author: str
    year: int | None = None
    genre: str | None = None

class BookOut(BookCreate):
    id: int
    model_config = ConfigDict(from_attributes=True)