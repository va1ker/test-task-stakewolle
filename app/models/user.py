import re
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import validates, relationship

from sqlalchemy.orm import declarative_base
from .base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(250), nullable=False)
    referal_code = Column(String(250), nullable=True)
    referal_id = Column(Integer, ForeignKey("users.id"))
    referral_code_expiration = Column(DateTime, nullable=True)
    referal = relationship("User", remote_side=[id])
