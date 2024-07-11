from fastapi import APIRouter,Depends,status
from fastapi.exceptions import HTTPException
from fastapi_jwt_auth import AuthJWT
from models import User,Order
from database import Session , engine
from fastapi.encoders import jsonable_encoder
from schemas import OrderModel

session=Session(bind=engine)
order_routes = APIRouter()

@order_routes.get('/')
async def hello(authorize:AuthJWT=Depends()):

    try:
        authorize.jwt_required()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Khong xa thuc duoc token"
        )
    return {"Message":"Hello mother fucker"}

@order_routes.post('/order',status_code=status.HTTP_201_CREATED)
async def place_an_order(order:OrderModel,authorize:AuthJWT=Depends()):
    try:
        authorize.jwt_required()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Khong xac thuc duoc token"
        )
    current_user = authorize.get_jwt_subject()
    user = session.query(User).filter(User.username==current_user).first()

    new_order=Order(
        quantity = order.quantity,
        pizza_size = order.pizza_size,
    )

    new_order.user = user
    session.add(new_order)
    session.commit()
    session.refresh(new_order)
    
    response= {
        "pizza_size":new_order.pizza_size,
        "quantity":new_order.quantity,
        "order_status":new_order.order_status,
        "user_id":new_order.user_id
    }
    return jsonable_encoder(response)

@order_routes.post('/order_all')
async def list_all_orders(authorize:AuthJWT=Depends()):
    try:
        authorize.jwt_required()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Khong xac thuc duoc token"
        )
    current_user = authorize.get_jwt_subject()
    user = session.query(User).filter(User.username==current_user).first()
    if user.is_staff:
        orders = session.query(object).all()
        return jsonable_encoder(orders)
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Khong phai nhan vien"
        )