from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "postgresql://myuser:mypassword@localhost:5432/mydb"
engine = create_engine(DATABASE_URL)

# Base class for ORM models
Base = declarative_base()
Session = sessionmaker(bind=engine)

# Define a table
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
