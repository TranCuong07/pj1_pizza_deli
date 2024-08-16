
from fastapi import APIRouter,Depends,status
from fastapi.exceptions import HTTPException
from database import get_db
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import session
from models import Category,Product
# from schemas import ListCategory

category_router = APIRouter()
# lay category
@category_router.get('/category')
async def list_category (db: session = Depends(get_db)):
    categories  = db.query(Category).all()

    if not categories:
        raise HTTPException(status_code=404, detail="No categories found")
    
    return jsonable_encoder(categories)

# lay product


# @category_router.get('/category_all/{id}')
# async def get_product_bycategory (id: int,db: session = Depends(get_db)):
#     categories = db.query(Category).filter(Category.id == id).first()

#     if not categories:
#         raise HTTPException(status_code=404, detail="No ca categories found")
#     product = db.query(Product).filter(Product.category_id == categories.id).all()

#     return jsonable_encoder(product)

@category_router.get('/product_category/{slug}')
async def get_product_bycategory (slug: str,db: session = Depends(get_db)):
    categories = db.query(Category).filter(Category.slug == slug).first()
    if not categories:
        raise HTTPException(status_code=404, detail="No ca categories found")
    product = db.query(Product).filter(Product.category_id == categories.id).all()
    return jsonable_encoder(product)

@category_router.get('/products')
async def list_category (db: session = Depends(get_db)):
    products  = db.query(Product).filter(Product.category).all()

    if not products:
        raise HTTPException(status_code=404, detail="No categories found")
    
    return jsonable_encoder(products)





