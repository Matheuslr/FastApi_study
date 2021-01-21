from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID

import uuid

from .database import Base

class User(Base):
  __tablename__ = "users"

  id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)
  email = Column(String, unique=True, index=True)
  hashed_password = Column(String)
  is_active = Column(Boolean, default=True)
  created_at = Column(DateTime(timezone=True), server_default=func.now())
  updated_at = Column(DateTime(timezone=True), on_update=func.now())

  items = relationship("Item", back_populates="owner")


class Item(Base):
  __tablename__ = "items"

  id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)
  title = Column(String, index=True)
  description = Column(String, index=True)
  owner_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
  created_at = Column(DateTime(timezone=True), server_default=func.now())
  updated_at = Column(DateTime(timezone=True), on_update=func.now())

  owner = relationship("User", back_populates="items")