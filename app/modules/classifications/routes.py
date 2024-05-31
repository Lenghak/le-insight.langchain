import json
from typing import Annotated
from fastapi import APIRouter, Query
from langchain.prompts.prompt import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

from core.llm import OllamaLLM
from utils.constants.labelling_templates import (
    CATEGORY_INPUT_TEMPLATE,
    CATEGORY_RESPONSE_FORMAT,
)

from .models import Articles
from .utils import LLMModels, clean_text


router = APIRouter(prefix="/classifications", tags=["Labellings"])


@router.post(path="/generate")
async def generate(
    body: Articles,
    model: Annotated[
        LLMModels,
        Query(),
    ] = "phi3",
):
    print(body)

    cleaned_input = clean_text(body.article)

    llm = OllamaLLM.get_instance(model=model)

    prompt_template = PromptTemplate(
        input_variables=["response_format", "categories", "article"],
        template=CATEGORY_INPUT_TEMPLATE,
    )

    chain = prompt_template | llm

    response = await chain.ainvoke(
        input={
            "article": cleaned_input,
            "categories": body.categories,
            "response_format": CATEGORY_RESPONSE_FORMAT,
        }
    )

    print(response)

    return json.loads(response)
