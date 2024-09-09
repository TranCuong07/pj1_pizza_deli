from fastapi import APIRouter,Depends,status, Request
from fastapi.exceptions import HTTPException
from fastapi_jwt_auth import AuthJWT
from database import get_db
from fastapi.encoders import jsonable_encoder
from schemas import OrderModel,OrderModelStatus,OrderCreateModel,OrderModel,CartData
from sqlalchemy.orm import session
from typing import List
from seapay import (SO_TAI_KHOAN,NGAN_HANG,TEMPLATE,DOWNLOAD)

order_router = APIRouter()

def verify_jwt(authorize:AuthJWT=Depends()):
        try:
             authorize.jwt_required()
             print("JWT Subject:", authorize.get_jwt_subject())  # In ra thông tin token
        except Exception as e:
                print("JWT Subject:", authorize.get_jwt_subject())  # In ra thông tin token
                raise HTTPException(
                 status_code=status.HTTP_401_UNAUTHORIZED,
                 detail="Khong xac thuc duoc token"
         )
         # tra ve thong tin nguoi dung tu jwt
        return authorize.get_jwt_subject()



@order_router.get('/check-cookie')
def verify_token_from_cookie(request: Request,authorize:AuthJWT=Depends()):
    token = request.cookies.get("access_token")
    print(f"Access token from cookie: {token}")
    if not token:
        raise HTTPException(status_code=400, detail="Cookie không tồn tại")

    try:
        authorize._token = token
        authorize.jwt_required()
        user_id = authorize.get_jwt_subject()
        return user_id
    except Exception as e:
        raise HTTPException(status_code=401, detail=f"Token không hợp lệ: {str(e)}")

# def verify_jwt(authorize: AuthJWT = Depends()):

#     try:
#         # Kiểm tra và xác minh token từ cookie
#         authorize.jwt_required()
        
#         # Lấy thông tin từ JWT sau khi xác thực thành công
#         user_id = authorize.get_jwt_subject()
#         print(f"User ID from Token: {user_id}")

#         return user_id
#     except Exception as e:
#         print(f"JWT Verification Error: {str(e)}")
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Khong xac thuc duoc token"
#         )

    
# @order_router.post('/order',status_code=status.HTTP_201_CREATED)
# async def place_an_order1(order:OrderModel,current_user: str = Depends(verify_jwt),
#     db: session = Depends(get_db)):
#     user = db.query(User).filter(User.username==current_user).first()

#     new_order=Order(
#         quantity = order.quantity,
#         pizza_size = order.pizza_size,
#     )

#     new_order.user = user
#     db.add(new_order)
#     db.commit()
#     db.refresh(new_order)
    
#     response= {
#         "pizza_size":new_order.pizza_size,
#         "quantity":new_order.quantity,
#         "order_status":new_order.order_status,
#         "user_id":new_order.user_id
#     }
#     return jsonable_encoder(response)

@order_router.post('/order',status_code=status.HTTP_201_CREATED)
async def place_an_order(order:OrderCreateModel,
    db: session = Depends(get_db)):
    user = db.query(User).filter(User.email==current_user).first()

    new_order = Order(

        id=str(uuid4()),
        price = order.price,
        products = order.products,
        user_email = order.user_email,
        payment_status = order.payment_status
    )

    new_order.user = user
    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    response= {
        "price":new_order.price,
        "products":new_order.products,
        "user_email":new_order.user_email,
        "payment_status":new_order.payment_status
    }
    return jsonable_encoder(response)

# @order_router.post('/qr-code',status_code=status.HTTP_201_CREATED)
# async def created_qr(cart_data:CartData,authorize: AuthJWT = Depends(verify_jwt)):
#     user_email = authorize
#     print("User email from JWT:", user_email)
#     SO_TIEN = cart_data.totalPrice
#     NOI_DUNG = cart_data.lastUpdated  
#     payment_url = f"https://qr.sepay.vn/img?acc={SO_TAI_KHOAN}&bank={NGAN_HANG}&amount={SO_TIEN}&des={NOI_DUNG}&template={TEMPLATE}&download={DOWNLOAD}"
#     return {"success": True, "qrCodeUrl": payment_url }




@order_router.post('/order_all',response_model=List[OrderModel])
async def list_all_orders(current_user: str = Depends(verify_jwt),
    db: session = Depends(get_db)):
    user = db.query(User).filter(User.username==current_user).first()
    if user.is_admin:
        orders = db.query(Order).all()
        return jsonable_encoder(orders)
    else:
        orders = db.query(Order).filter(Order.user_email==user_email).all()
        return jsonable_encoder(orders)

# lay order theo id (lay 01 order khi da biet id)
@order_router.get('/order/{id}')
async def get_order_by_id(id:int,current_user: str = Depends(verify_jwt),
    db: session = Depends(get_db)):
    user = db.query(User).filter(User.username==current_user).first()
    if not user or not user.is_staff: #check phai la nhan vien khong
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="vui long dang nhap"
        )
    order = db.query(Order).filter(Order.id==id).first() #lay order theo id
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="khong tim thay order"
            )
    return jsonable_encoder(order)

# lay order theo user
@order_router.get('/user/order')
async def get_user_orders(
    current_user: str = Depends(verify_jwt),
    db: session = Depends(get_db)):
    user = db.query(User).filter(User.username==current_user).first() # lay thong tin kh theo token
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="nguoi dung khong ton tai"
        )
        #tra ve oerder theo khach hang
    return jsonable_encoder(user.orders)

#update order
@order_router.put('/order/update/{order_id}/')
async def update_order(id:int,order:OrderModel,current_user: str = Depends(verify_jwt),
    db: session = Depends(get_db)):

    order_to_update = db.query(Order).filter(Order.id==id).first() #lay order theo id
    if not order_to_update:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="khong tim thay order"
            )

    order_to_update.quantity = order.quantity
    order_to_update.pizza_size = order.pizza_size
    db.commit()
    return jsonable_encoder(order_to_update)


# update order status
@order_router.put('/order/status/{order_id}/')
async def update_order_status(id:int,order:OrderModelStatus,current_user: str = Depends(verify_jwt),
    db: session = Depends(get_db)):
    user = db.query(User).filter(User.username==current_user).first()
    if not user or not user.is_staff: #check phai la nhan vien khong
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Khong phai nhan vien"
        )
    order_to_update_status = db.query(Order).filter(Order.id==id).first() #lay order theo id
    if not order_to_update_status:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="khong tim thay order"
            )
    order_to_update_status.order_status = order.order_status
    db.commit()
    response= {
        "pizza_size":order_to_update_status.pizza_size,
        "quantity":order_to_update_status.quantity,
        "order_status":order_to_update_status.order_status,
    }
    return jsonable_encoder(response)

@order_router.delete('/order/delete/{id}/',status_code=status.HTTP_204_NO_CONTENT)
async def delete_order(id:int,current_user: str = Depends(verify_jwt),
    db: session = Depends(get_db)):
    user = db.query(User).filter(User.username==current_user).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="tai khoan khong ton tai"
        )
    order_to_delete = db.query(Order).filter(Order.id==id).first() #lay order theo id
    if not order_to_delete:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="khong tim thay order"
        )
    db.delete(order_to_delete)
    db.commit()
    response= {
       "Message":"Xoa thanh cong"
    }
    return jsonable_encoder(order_to_delete)
