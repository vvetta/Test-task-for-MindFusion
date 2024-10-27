from src.settings import DATABASE_URL, DATABASE_ECHO

from sqlalchemy import Integer, Column, DateTime
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession


class BaseModel(DeclarativeBase):
    __abstract__ = True

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True, index=True)
    time_created = Column(DateTime(timezone=True), server_default=func.now()) 
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())


async_engine = create_async_engine(DATABASE_URL, echo=DATABASE_ECHO)
async_session = async_sessionmaker(async_engine, expire_on_commit=True)


async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session
