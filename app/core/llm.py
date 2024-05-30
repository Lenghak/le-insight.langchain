import logging

from langchain_community.llms.ollama import Ollama
from langchain_openai import ChatOpenAI
from pydantic.v1 import SecretStr

from core.config import Settings
from modules.classifications.utils import LLMModels


# The `OpenAILLM` class is a singleton class that provides a method `getInstance` to retrieve an
# instance of the class.
class OpenAILLM:

    @classmethod
    def get_instance(cls):
        if cls._instance == None:
            cls._instance = ChatOpenAI(
                api_key=SecretStr(Settings.get_instance().OPENAI_API_KEY)
            )
        return cls._instance


# This Python class `OllamaLLM` implements a singleton pattern to ensure only one instance of the
# class is created.
class OllamaLLM:

    _instance = None
    _model_name = None

    @classmethod
    def get_instance(
        cls,
        model: LLMModels,
    ):
        if cls._instance == None or cls._model_name != model:
            cls._instance = Ollama(model=model, format="json", temperature=0)
            cls._model_name = model

        return cls._instance
