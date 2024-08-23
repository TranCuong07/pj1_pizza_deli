from fastapi import FastAPI,Depends
from order_routes import order_router
from auth_routes import auth_routes
from category_routes import category_router
from products_routes import products_routes
from fastapi_jwt_auth import AuthJWT
from schemas import Setting
import re
import inspect
from fastapi.routing import APIRoute
from fastapi.openapi.utils import get_openapi
from bearer import custom_openapi
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware


app = FastAPI()

# cors
origins = [
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# beaerer
app.openapi = lambda: custom_openapi(app)

@AuthJWT.load_config
def get_config():
    return Setting()


app.include_router(order_router, prefix="/order")
app.include_router(auth_routes, prefix="/auth")
app.include_router(category_router, prefix="/category")
app.include_router(products_routes, prefix="/products")