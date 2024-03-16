from core.config import Settings
from langchain_community.llms.ollama import Ollama
from langchain_openai import ChatOpenAI
from pydantic.v1 import SecretStr


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


# This Python class `Llama2LLM` implements a singleton pattern to ensure only one instance of the
# class is created.
class Llama2LLM:

    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance == None:
            cls._instance = Ollama(
                model="llama2", format="json", temperature=0
            )

        return cls._instance


# This Python class `Llama2LLM` implements a singleton pattern to ensure only one instance of the
# class is created.
class MistralLLM:

    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance == None:
            cls._instance = Ollama(
                model="mistral", format="json", temperature=0
            )

        return cls._instance
