from sqlalchemy import Column, Integer, String, Boolean, ForeignKey,DECIMAL,JSON, DateTime
from sqlalchemy.orm import relationship
from database import Base
from sqlalchemy_utils.types import ChoiceType
import datetime

class User(Base):
    __tablename__ = "user" #tao bang user
    id = Column(Integer,primary_key=True)
    username = Column(String(25),unique=True)
    email = Column(String,unique=True)
    password = Column(String,nullable=True)
    is_active = Column(Boolean,default=False)
    is_staff = Column(Boolean,default=False)
    orders = relationship('Order',back_populates='user') #tao moi lien ket user vs order
    
    def __repr__(self):
        return f"<User {self.username}?"

class Category(Base):
    __tablename__ = "category" #tao Category
    id = Column(Integer,primary_key=True, default = 'cuid()')
    createdAt = Column(DateTime, default = datetime.datetime.utcnow)
    title = Column (String)
    desc = Column(String)
    color = Column(String)
    img = Column(String)
    slug = Column(String, unique=True)
    product = relationship('Product',back_populates='category') #tao moi lien ket

class Product(Base):
    __tablename__ = "product" #tao Product
    id = Column(Integer,primary_key=True, default = 'cuid()')
    createdAt = Column(DateTime, default = datetime.datetime.utcnow)
    title = Column (String)
    desc = Column(String)
    img = Column(String)
    price = Column(DECIMAL)
    isFeatured = Column(Boolean, default= False)
    options = Column(JSON)
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship('Category',back_populates='product') #tao moi lien ket 

class Order(Base):
    __tablename__ = "orders" #tao Product
    id = Column(Integer,primary_key=True, default = 'cuid()')
    createdAt = Column(DateTime, default = datetime.datetime.utcnow)
    price = Column(DECIMAL)
    products = Column(JSON)
    status = Column(String)
    intent_id = Column(String, unique=True, nullable=True)
    user_id = Column(Integer, ForeignKey('user.id'))

    user = relationship("User", back_populates="orders")

    def __repr__(self):
        return f"<Order {self.id}>"