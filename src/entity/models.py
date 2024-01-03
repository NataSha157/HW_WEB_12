import enum

from datetime import date
from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Date, Integer, ForeignKey, DateTime, func
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


# class Contact(Base):
#     __tablename__ = 'contacts'
#     id: Mapped[int] = mapped_column(primary_key=True)
#     firstname: Mapped[str] = mapped_column(String(50))
#     lastname: Mapped[str] = mapped_column(String(50), index=True)
#     e_mail: Mapped[str] = mapped_column(String(120), index=True, unique=True)
#     birthday: Mapped[date] = mapped_column(Date())
#     add_data: Mapped[Optional[str]] = mapped_column(String(250))


class Contact(Base):
    __tablename__ = 'contacts'
    id: Mapped[int] = mapped_column(primary_key=True)
    firstname: Mapped[str] = mapped_column(String(50))
    lastname: Mapped[str] = mapped_column(String(50), index=True)
    e_mail: Mapped[str] = mapped_column(String(120), index=True, unique=True)
    birthday: Mapped[date] = mapped_column(Date())
    add_data: Mapped[Optional[str]] = mapped_column(String(250))
    created_at: Mapped[date] = mapped_column('created_at', DateTime, default=func.now(), nullable=True)
    update_at: Mapped[date] = mapped_column('update_at', DateTime, default=func.now(), onupdate=func.now(), nullable=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'), nullable=True)
    user: Mapped['User'] = relationship('User', backref='contacts', lazy='joined')


# class Role(enum.Enum):
#     admin: str = "admin"
#     moderator: str = "moderator"
#     user: str = "user"

class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(150), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    avatar: Mapped[str] = mapped_column(String(255), nullable=True)
    refresh_token: Mapped[str] = mapped_column(String(255), nullable=True)
    created_at: Mapped[date] = mapped_column('created_at', DateTime, default=func.now())
    update_at: Mapped[date] = mapped_column('update_at', DateTime, default=func.now(), onupdate=func.now())