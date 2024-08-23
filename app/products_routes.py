
from fastapi import APIRouter,Depends,status
from fastapi.exceptions import HTTPException
from database import get_db
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import session
from models import Category,Product

products_routes = APIRouter()

@products_routes.get('/products')
async def getAll_products (db: session = Depends(get_db)):
    products  = db.query(Product).filter(Product.category).all()

    if not products:
        raise HTTPException(status_code=404, detail="No categories found")
    
    return jsonable_encoder(products)

@products_routes.get('/products/{id}')
async def getProduct_byID (id: int,db: session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == id).first()
    if not product:
        raise HTTPException(status_code=404, detail="No product found")
    return jsonable_encoder(product)
