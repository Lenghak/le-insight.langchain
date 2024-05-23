from pydantic import BaseModel


class Articles(BaseModel):
    article: str
    categories: list[str]
