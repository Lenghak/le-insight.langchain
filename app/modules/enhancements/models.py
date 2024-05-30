from typing import Annotated
from fastapi import Body
from pydantic import BaseModel, constr


class EnhancementBody(BaseModel):
    article: Annotated[
        str,
        Body(title="The part of article that needed to be enhance", max_length=2000),
    ]
