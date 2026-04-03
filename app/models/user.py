from sqlalchemy import Column,Integer,String,Boolean
from app.db.session import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__= "users"

    id = Column(Integer,primary_key=True,index=True)
    username = Column(String,nullable=False)
    email = Column(String,unique=True,nullable=False)
    password = Column(String)
    role = Column(String,default='viewer')
    is_active = Column(Boolean,default=True)
    
    transactions = relationship("Transaction", back_populates="owner")


