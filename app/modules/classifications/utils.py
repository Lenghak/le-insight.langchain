import string
from typing import Literal

LLMModels = Literal[
    "llama2",
    "llama3",
    "llama3:text",
    "llama3:70b",
    "mistral",
    "mixstral",
    "phi3",
    "phi3:mini-128k",
    "phi3:medium",
]


def clean_text(text):
    # Removing punctuations using replace() method
    for punctuation in string.punctuation:
        text = text.replace(punctuation, "")

    return text
