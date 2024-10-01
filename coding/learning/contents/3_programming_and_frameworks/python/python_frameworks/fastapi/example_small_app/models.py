from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    # tells SQLAlchemy the name of the table to use in the database for each of these models.
    __tablename__ = "users"

    # Create model attributes/columns
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    # Create the relationships between these models
    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    # Create model attributes/columns
    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    # relationship to the User model
    owner = relationship("User", back_populates="items")
