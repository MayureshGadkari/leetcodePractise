from sqlalchemy import Boolean,Column,ForeignKey,Integer,String
from sqlalchemy.orm import relationship

from database_connection import Base

class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String)
    phone_number = Column(Integer)
    email_id = Column(String)
    is_active = Column(Boolean, default=True)
    gender = Column(String)

    vehicles = relationship("Vehicle", back_populates="owner")


class Vehicle(Base):
    __tablename__ = "Vehicles"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String, index=True)
    model = Column(String)
    plate_number = Column(String, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))

    owner = relationship("User", back_populates="vehicles")