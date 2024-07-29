from fastapi import APIRouter,Depends,status
from fastapi.exceptions import HTTPException
from fastapi_jwt_auth import AuthJWT
from models import User,Order
from database import Session , engine
from fastapi.encoders import jsonable_encoder
from schemas import OrderModel,OrderModelStatus

session=Session(bind=engine)
order_router = APIRouter()

def verify_jwt(authorize:AuthJWT=Depends()):
        try:
            authorize.jwt_required()
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Khong xac thuc duoc token"
        )
        # tra ve thong tin nguoi dung tu jwt
        return authorize.get_jwt_subject()
    
@order_router.post('/order',status_code=status.HTTP_201_CREATED)
async def place_an_order(order:OrderModel,current_user: str = Depends(verify_jwt)):
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

@order_router.post('/order_all')
async def list_all_orders(current_user: str = Depends(verify_jwt)):
    user = session.query(User).filter(User.username==current_user).first()
    if user.is_staff:
        orders = session.query(Order).all()
        return jsonable_encoder(orders)
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Khong phai nhan vien"
        )
# lay order theo id (lay 01 order khi da biet id)
@order_router.get('/order/{id}')
async def get_order_by_id(id:int,current_user: str = Depends(verify_jwt)):
    user = session.query(User).filter(User.username==current_user).first()
    if not user or not user.is_staff: #check phai la nhan vien khong
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Khong phai nhan vien"
        )
    order = session.query(Order).filter(Order.id==id).first() #lay order theo id
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="khong tim thay order"
            )
    return jsonable_encoder(order)

# lay order theo user
@order_router.get('/user/order')
async def get_user_orders(current_user: str = Depends(verify_jwt)):
    user = session.query(User).filter(User.username==current_user).first() # lay thong tin kh theo token
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="nguoi dung khong ton tai"
        )
        #tra ve oerder theo khach hang
    return jsonable_encoder(user.orders)

#update order
@order_router.put('/order/update/{order_id}/')
async def update_order(id:int,order:OrderModel,current_user: str = Depends(verify_jwt)):

    order_to_update = session.query(Order).filter(Order.id==id).first() #lay order theo id
    if not order_to_update:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="khong tim thay order"
            )

    order_to_update.quantity = order.quantity
    order_to_update.pizza_size = order.pizza_size
    session.commit()
    return jsonable_encoder(order_to_update)


# update order status
@order_router.put('/order/status/{order_id}/')
async def update_order_status(id:int,order:OrderModelStatus,current_user: str = Depends(verify_jwt)):
    user = session.query(User).filter(User.username==current_user).first()
    if not user or not user.is_staff: #check phai la nhan vien khong
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Khong phai nhan vien"
        )
    order_to_update_status = session.query(Order).filter(Order.id==id).first() #lay order theo id
    if not order_to_update_status:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="khong tim thay order"
            )
    order_to_update_status.order_status = order.order_status
    session.commit()
    response= {
        "pizza_size":order_to_update_status.pizza_size,
        "quantity":order_to_update_status.quantity,
        "order_status":order_to_update_status.order_status,
    }
    return jsonable_encoder(response)

@order_router.delete('/order/delete/{id}/',status_code=status.HTTP_204_NO_CONTENT)
async def delete_order(id:int,current_user: str = Depends(verify_jwt)):
    user = session.query(User).filter(User.username==current_user).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="tai khoan khong ton tai"
        )
    order_to_delete = session.query(Order).filter(Order.id==id).first() #lay order theo id
    if not order_to_delete:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="khong tim thay order"
        )
    session.delete(order_to_delete)
    session.commit()
    response= {
       "Message":"Xoa thanh cong"
    }
    return jsonable_encoder(order_to_delete)