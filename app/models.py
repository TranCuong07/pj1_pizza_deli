from sqlalchemy import Column, Integer, String, Boolean, ForeignKey,DECIMAL,JSON, DateTime,Numeric,Text,UniqueConstraint,Enum
from sqlalchemy.orm import relationship
from database import Base
from sqlalchemy_utils.types import ChoiceType
import datetime
import uuid
from sqlalchemy.dialects.postgresql import UUID
import enum



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

class PaymentStatus(enum.Enum):
    UNPAID = "Unpaid"
    PAID = "Paid"
    CANCELLED = "Cancelled"
    REFUNDED = "Refunded"

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
    __tablename__ = 'order'
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    price = Column(Numeric)
    products = Column(JSON)
    status = Column(String)
    payment_status = Column(Enum(PaymentStatus), default=PaymentStatus.UNPAID, nullable=False)
    intent_id = Column(String, unique=True, nullable=True)
    user_email = Column(String, ForeignKey('user.email'), nullable=False)
    
    # Mối quan hệ với User, sử dụng back_populates
    user = relationship('User', back_populates='orders')



class User(Base):
    __tablename__ = 'user'
    
    id = Column(String, primary_key=True, default='cuid')  # Sử dụng String cho ID
    name = Column(String, nullable=True)
    email = Column(String, unique=True, nullable=True)
    email_verified = Column(DateTime, nullable=True)
    image = Column(String, nullable=True)
    is_admin = Column(Boolean, default=False)
    
    accounts = relationship('Account', back_populates='user')
    sessions = relationship('Session', back_populates='user')
    orders = relationship('Order', back_populates='user')

class Session(Base):
    __tablename__ = 'session'
    
    id = Column(String, primary_key=True, default='cuid')  # Sử dụng String cho ID
    session_token = Column(String, unique=True, nullable=False)
    user_id = Column(String, ForeignKey('user.id'), nullable=False)  # Sử dụng String cho FK
    expires = Column(DateTime, nullable=False)

    user = relationship('User', back_populates='sessions')


class Account(Base):
    __tablename__ = 'account'
    
    id = Column(String, primary_key=True, default='cuid')
    user_id = Column(String, ForeignKey('user.id'), nullable=False)
    type = Column(String, nullable=False)
    provider = Column(String, nullable=False)
    provider_account_id = Column(String, nullable=False)
    refresh_token = Column(Text, nullable=True)
    access_token = Column(Text, nullable=True)
    expires_at = Column(Integer, nullable=True)
    token_type = Column(String, nullable=True)
    scope = Column(String, nullable=True)
    id_token = Column(Text, nullable=True)
    session_state = Column(String, nullable=True)

    user = relationship('User', back_populates='accounts')

    __table_args__ = (
        UniqueConstraint('provider', 'provider_account_id', name='uix_provider_account_id'),
    )
class VerificationToken(Base):
    __tablename__ = 'verification_token'
    id = Column(String, primary_key=True, default='cuid')
    identifier = Column(String, nullable=False)
    token = Column(String, unique=True, nullable=False)
    expires = Column(DateTime, nullable=False)

    __table_args__ = (
        UniqueConstraint('identifier', 'token', name='uix_identifier_token'),
    )
    