"""
  The code defines a FastAPI application instance.
"""

import uvicorn
from core import config
from fastapi import FastAPI

app = FastAPI()
setting = config.SingletonSettings.get_instance()


@app.get("/")
async def root():
    """
    This Python function uses the FastAPI framework to create a route that returns a JSON response
    with the message "Hello World" when the root URL is accessed.
    :return: The code is returning a JSON object with a key "message" and value "Hello World".
    """
    return {"message": setting.APP_NAME}


def main():
    """
    The above function defines a main function using FastAPI in Python.
    """

    uvicorn.run(
        "main:app",
        port=8000,
        log_level="info",
        workers=8,
        reload=(setting.ENV == "development"),
    )


if __name__ == "__main__":
    main()
