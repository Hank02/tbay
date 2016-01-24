from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey

# create engine that will talk to DB using raw SQL
engine = create_engine('postgresql://ubuntu:thinkful@localhost:5432/tbay')
# create session - like psycopg2, allows use of DB transacions
Session = sessionmaker(bind=engine)
session = Session()
# acts like repository for the models to build DB's table structure
Base = declarative_base()

# table to store all the users
class User(Base):
    __tablename__ = "user"
    
    # create table columns
    id = Column(Integer, primary_key = True)
    username = Column(String, nullable = False)
    password = Column(String, nullable = False)
    
    # one-to-many relationship with items (A)
    items = relationship("Item", backref = "user")
    # one-to-many relationship with bids (B)
    bids = relationship("Item", backref = "user")

# table to store items
class Item(Base):
    __tablename__ = "items"
    
    # create table columns
    id = Column(Integer, primary_key = True)
    name = Column(String, nullable = False)
    description = Column(String)
    start_time = Column(DateTime, default = datetime.utcnow)
    
    # complete one-to-many relationship between users and items (A)
    user_id = Column(Integer, ForeignKey('user.id'), nullable = False)
    # one-to-many relationship with bids (C)
    bids = relationship("Bid", backref = "item")

# table to store bids
class Bid(Base):
    __tablename__ = "bid"
    
    # create table columns
    id = Column(Integer, primary_key = True)
    price = Column(Float, nullable = False)
    
    # complete one-to-many relationship between users and bids (B)
    user_id = Column(Integer, ForeignKey('user.id'), nullable = False)
    # complete one-to-many relationship between item and bids (C)
    item_id = Column(Integer, ForeignKey('item.id'), nullable = False)

# create tables
Base.metadata.create_all(engine)