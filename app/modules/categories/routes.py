import json

from fastapi import APIRouter, HTTPException
from fastapi.logger import logger
from core.context import context

from .models import Articles
from .utils import clean_text


router = APIRouter(prefix="/categories", tags=["Categories"])


@router.post(path="/generate")
async def generate(
    body: Articles,
):
    cleaned_input = clean_text(body.article)

    llm = context.get("llm_dependency")

    if not llm:
        raise HTTPException(500, "LLM is not initialized")

    chain = llm.get("chain")

    response = await chain.ainvoke(
        input={
            "article": cleaned_input,
            "categories": body.categories,
            "response_format": llm.get("response_format"),
        }
    )

    logger.info(response)

    return json.loads(response)
