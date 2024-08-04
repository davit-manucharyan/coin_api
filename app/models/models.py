from database import Base

from sqlalchemy import Column, Integer, String, ForeignKey, text, Float, Boolean
from sqlalchemy.sql.sqltypes import TIMESTAMP


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, nullable=False, primary_key=True)
    user_name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    status = Column(Boolean, nullable=True, server_default="False")
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("now()"))
