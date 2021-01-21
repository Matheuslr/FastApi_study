from typing import List, Optional

from pydantic import BaseModel, UUID4


class ItemBase(BaseModel):
  title: str
  description: Optional[str] = None


class ItemCreate(ItemBase):
  pass


class Item(ItemBase):
  id: UUID4
  owner_id: UUID4

  class Config:
    orm_mode = True


class UserBase(BaseModel):
  email: str


class UserCreate(UserBase):
  password: str


class User(UserBase):
  id: UUID4
  is_active: bool
  items: List[Item] = []

  class Config:
    orm_mode = True