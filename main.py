from fastapi import FastAPI
from order_routes import order_routes
from auth_routes import auth_routes

app = FastAPI()

app.include_router(order_routes, prefix="/order")
app.include_router(auth_routes, prefix="/auth")

@app.get("/")
async def root():
    return {"message": "Hello World"}