"""
This is the start of the application modules where all initializations are taking places
"""

import uvicorn
from core import config
from fastapi import FastAPI
from routes import create_routes

# The code snippet `app = FastAPI()` creates an instance of the FastAPI class, which represents a
# FastAPI application.
app = FastAPI()

# `setting = config.SingletonSettings.get_instance()` is a line of code that is likely retrieving an
# instance of a SingletonSettings class from the config module.
setting = config.Settings.get_instance()

# `create_routes(app)` is a function that is responsible for setting up and defining the routes for
# the FastAPI application instance `app`.This function helps organize the routing logic within the FastAPI application.
create_routes(app)


if __name__ == "__main__":
    """
    The above function defines a main function using FastAPI in Python.
    """
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        log_level="info",
        workers=8,
        reload=(setting.ENV == "development"),
    )
