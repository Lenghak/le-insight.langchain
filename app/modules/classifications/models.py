from typing import Literal
from pydantic import BaseModel, Field


class Articles(BaseModel):
    article: str
    categories: list[str]
