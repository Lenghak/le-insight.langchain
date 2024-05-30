from typing import TypedDict

from core.llm import OllamaLLM
from langchain.chains.llm import LLMChain
from langchain.prompts.prompt import PromptTemplate
from langchain_community.llms.ollama import Ollama


class LlmChainDependency(TypedDict):
    ollama: Ollama
    input_template: str
    response_format: dict[str, list[dict[str, str]]]
    prompt_template: PromptTemplate
    category_chain: LLMChain
