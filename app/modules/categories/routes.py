import json

from typing import Annotated
from fastapi import Depends, APIRouter

from .utils import clean_text
from .models import Articles
from .dependecies import LlmChainDependency, llm_chain as llm_chain_dependency
from spacy import load

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.post(path="/generate")
async def generate(
    body: Articles,
    llm_chain: Annotated[
        LlmChainDependency, Depends(dependency=llm_chain_dependency, use_cache=True)
    ],
):
    cleaned_input = clean_text(body.article)

    response = await llm_chain.get("category_chain").abatch(
        [
            {
                "article": cleaned_input,
                "response_format": llm_chain.get("response_format"),
            }
        ]
    )

    return json.loads(response[0]["text"])
