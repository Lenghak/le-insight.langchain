""" 
The class `_Settings` defines configuration settings for a Python application using Pydantic, 
with a singleton pattern implemented in the `SingletonSettings` class.
"""

from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class _Settings(BaseSettings):
    APP_NAME: str
    ENV: Literal["production", "development"]

    model_config = SettingsConfigDict(env_file=".env")


class SingletonSettings:
    """
    The above class is a SingletonSettings class that ensures only one instance of _Settings
    is created and provides a method to access that instance.
    """

    _instance = None

    @classmethod
    def get_instance(cls):
        """
        The above function is a class method that returns an instance of the `_Settings` class,
        creating it if it doesn't already exist.

        :param cls: In the given code snippet, `cls` refers to the class itself.
        It is a reference to the class object and is commonly used in class methods to access
        class variables and methods
        :return: The `get_instance` method is returning an instance of the `_Settings` class.
        """
        if not cls._instance:
            cls._instance = _Settings()  # type: ignore - - The env will be loaded automatically
        return cls._instance
