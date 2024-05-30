from typing import TypedDict
from fastapi import FastAPI
from langchain.prompts.prompt import PromptTemplate
from langchain_core.runnables.base import RunnableSerializable
from langchain_community.llms.ollama import Ollama
from langchain_community.chat_message_histories.redis import RedisChatMessageHistory
from langchain.globals import set_verbose
from contextlib import asynccontextmanager


class LlmBaseHistory(TypedDict):
    base_history: RedisChatMessageHistory
    base_session_id: str


class LlmChainDependency(TypedDict):
    ollama: Ollama
    input_template: str
    response_format: dict[str, list[dict[str, str]]]
    prompt_template: PromptTemplate
    history: LlmBaseHistory
    chain: RunnableSerializable


class Context(TypedDict):
    llm_dependency: LlmChainDependency | None


context: Context = {"llm_dependency": None}


@asynccontextmanager
async def lifespan(app: FastAPI):
    set_verbose(True)
    yield
