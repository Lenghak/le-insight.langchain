import json
from typing import Annotated

from fastapi import APIRouter, Query
from fastapi.logger import logger

from core.llm import OllamaLLM
from modules.classifications.utils import LLMModels

from .models import EnhancementBody

router = APIRouter(prefix="/enhancements", tags=["Enhancements"])


@router.post(path="/enhance")
async def generate(
    body: EnhancementBody,
    model: Annotated[
        LLMModels,
        Query(),
    ] = "phi3",
):
    llm = OllamaLLM.get_instance(model=model)

    for chunk in llm.stream(body.article):
        print(chunk, end="", flush=True)
