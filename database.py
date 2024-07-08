# database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

# Get the database URL from environment variables
DATABASE_URL = os.environ.get("SUPABASE_DATABASE_URL")

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL,echo=True)

# Create a session factory
Session = sessionmaker()

# Create a base class for declarative ORM models
Base = declarative_base()
