from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, ForeignKey, Column, Integer
from ..connect import engine


class Base(DeclarativeBase):
    pass


class TokenUser(Base):
    __tablename__ = "token_user"

    id: Mapped[int] = mapped_column(primary_key=True)
    token: Mapped[str] = mapped_column(String(30))


class UserFileStorage(Base):
    __tablename__ = "filestorage_user"

    id: Mapped[int] = mapped_column(primary_key=True)
    user: Mapped[int] = mapped_column(ForeignKey("token_user.id"))
    name: Mapped[str] = mapped_column(String(60))
    size: Mapped[str] = mapped_column(String(30))
    path: Mapped[str] = mapped_column(String(400))
    disc: Mapped[str] = mapped_column(String(400))


Base.metadata.create_all(engine, checkfirst=True)
