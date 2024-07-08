from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from sqlalchemy_utils.types import ChoiceType

class User(Base):
    __tablename__ = "User" #tao bang user
    id = Column(Integer,primary_key=True)
    username = Column(String(25),unique=True)
    email = Column(String,unique=True)
    password = Column(String,nullable=True)
    is_active = Column(Boolean,default=False)
    is_staff = Column(Boolean,default=False)
    Orders = relationship('Orders',back_populates='User') #tao moi lien ket user vs order
    
    def __repr__(self):
        return f"<User {self.username}?"

class Order(Base):
    #tao mot so value mac dinh
    ORDER_STATUS = [
        ('PENDING', 'pending'),
        ('IN-TRANSIT', 'in-transit'),
        ('DELIVERED', 'delivered')
    ]

    PIZZA_SIZE = [
        ('SMALL', 'small'),
        ('MEDIUM', 'medium'),
        ('LARGE', 'large'),
        ('EXTRA-LARGE', 'extra-large')
    ]

    __tablename__ = "Orders" #tao bang orders
    id = Column(Integer,primary_key=True)
    quantity = Column(Integer,unique=True)
    order_status = Column(ChoiceType(choices=ORDER_STATUS),default="PENDING")
    pizza_size = Column(ChoiceType(choices=PIZZA_SIZE),default="SMALL")
    user_id = Column(Integer,ForeignKey('User.id'))
    User = relationship('User',back_populates='Orders') #tao moi lien ket user vs order


    def __repr__(self):
        return f"<Orders {self.id}>"