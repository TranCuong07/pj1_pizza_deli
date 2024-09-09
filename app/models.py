from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DECIMAL, JSON, DateTime, Numeric, Text, UniqueConstraint, Enum, TIMESTAMP
from sqlalchemy.orm import relationship
from database import Base
from sqlalchemy_utils.types import ChoiceType
import datetime
import uuid
from sqlalchemy.dialects.postgresql import UUID
import enum

class Category(Base):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True, default=lambda: str(uuid.uuid4()))
    createdAt = Column(DateTime, default=datetime.datetime.utcnow)
    title = Column(String)
    desc = Column(String)
    color = Column(String)
    img = Column(String)
    slug = Column(String, unique=True)
    product = relationship('Product', back_populates='category')

class PaymentStatus(enum.Enum):
    UNPAID = "Unpaid"
    PAID = "Paid"
    CANCELLED = "Cancelled"
    REFUNDED = "Refunded"

class Product(Base):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True, default=lambda: str(uuid.uuid4()))
    createdAt = Column(DateTime, default=datetime.datetime.utcnow)
    title = Column(String)
    desc = Column(String)
    img = Column(String)
    price = Column(DECIMAL)
    isFeatured = Column(Boolean, default=False)
    options = Column(JSON)
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship('Category', back_populates='product')

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
    user = relationship('User', back_populates='orders')

class User(Base):
    __tablename__ = 'user'
    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
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
    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    session_token = Column(String, unique=True, nullable=False)
    user_id = Column(String, ForeignKey('user.id'), nullable=False)
    expires = Column(DateTime, nullable=False)
    user = relationship('User', back_populates='sessions')

class Account(Base):
    __tablename__ = 'account'
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
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
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    identifier = Column(String, nullable=False)
    token = Column(String, unique=True, nullable=False)
    expires = Column(DateTime, nullable=False)
    __table_args__ = (
        UniqueConstraint('identifier', 'token', name='uix_identifier_token'),
    )

class Transactions(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True)
    gateway = Column(String, nullable=False)
    transaction_date = Column(TIMESTAMP, default=datetime.datetime.utcnow)
    transaction_content = Column(String)
    account_number = Column(String, nullable=False)
    sub_account = Column(String, nullable=False)
    amount_in = Column(Numeric)
    amount_out = Column(Numeric)
    accumulated = Column(Numeric)
    code = Column(String)
    reference_number = Column(String)
    body = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
