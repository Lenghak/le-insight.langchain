import json

from fastapi import APIRouter, HTTPException

from core.context import context

from .models import Articles
from .utils import clean_text


router = APIRouter(prefix="/categories", tags=["Categories"])


@router.post(path="/generate")
async def generate(
    body: Articles,
):
    cleaned_input = clean_text(body.article)

    llm = context.get("category_llm_dependency")

    if not llm:
        raise HTTPException(500, "LLM is not initialized")

    response = await llm.get("category_chain").abatch(
        [
            {
                "article": cleaned_input,
                "response_format": llm.get("response_format"),
            }
        ]
    )

    return json.loads(response[0]["text"])
