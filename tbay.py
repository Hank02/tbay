from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime

# create engine that will talk to DB using raw SQL
engine = create_engine('postgresql://ubuntu:thinkful@localhost:5432/tbay')
# create session - like psycopg2, allows use of DB transacions
Session = sessionmaker(bind=engine)
session = Session()
# acts like repository for the models to build DB's table structure
Base = declarative_base()

class Item(Base):
    __tablename__ = "items"
    
    id = Column(Integer, primary_key = True)
    name = Column(String, nullable = False)
    description = Column(String)
    start_time = Column(DateTime, default = datetime.utcnow)

    
Base.metadata.create_all(engine)