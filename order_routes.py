from fastapi import APIRouter

order_routes = APIRouter()

@order_routes.get('/')
async def  hello():
    return {"test chức năng ord111er"}