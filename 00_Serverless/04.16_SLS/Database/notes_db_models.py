from sqlalchemy     import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy     import create_engine
from datetime       import datetime
from dotenv         import load_dotenv
import os

def get_current_time():
    return datetime.now()

# Load the .db_credentials file and get the variables:
load_dotenv(dotenv_path='Database/.db_credentials')
host = os.getenv('DB_HOST_IP')
port = os.getenv('DB_HOST_PORT')
user = os.getenv('DB_USERNAME')
pswd = os.getenv('DB_PASSWORD')
db   = os.getenv('DB_NAME')


# SQLAlchemy engine, session and base
engine  = create_engine(f'postgresql://{user}:{pswd}@{host}:{port}/{db}', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base    = declarative_base()


# Table Notes
class NotesTable(Base):
    __tablename__ = 'Notes_v2'
    NotesID     = Column(Integer, primary_key=True)
    UserID      = Column(ForeignKey('Users_v2.UserID'))
    Title       = Column(String(50),    nullable=False)
    Content     = Column(String(240),   nullable=False)
    DateCreated = Column(DateTime,      nullable=False)
    DateUpdated = Column(DateTime,      nullable=True)
    StatusNote  = Column(Boolean)


# Table Users
class UsersTable(Base):
    __tablename__ = 'Users_v2'
    UserID        = Column(Integer,    primary_key=True)
    UserName      = Column(String(50), nullable=False)
    LastName      = Column(String(50), nullable=False)
    Password      = Column(String(80), nullable=False)
    EmailAddress  = Column(String(50), nullable=True)
    SecretKey     = Column(String(32), nullable=False,  unique=True)
    DateCreated   = Column(DateTime,   default=get_current_time())
    StatusAccount = Column(Boolean,    default=True)


# Create table
Base.metadata.create_all(engine)

# Done
