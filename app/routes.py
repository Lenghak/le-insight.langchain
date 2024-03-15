from fastapi import FastAPI
from modules.categories.routes import router as categories_router

_routers = [categories_router]


def create_routes(app: FastAPI):
    """
    The function `create_routes` includes all routes in the `routes` list in the FastAPI app with the
    prefix "/api".

    :param app: The `app` parameter is an instance of the `FastAPI` class. It represents the FastAPI
    application that the routes will be added to
    :type app: FastAPI
    """
    for router in _routers:
        app.include_router(router, prefix="/api")
