from typing import Optional

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import  DeclarativeBase, Mapped, mapped_column

from datetime import datetime
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

engine =  create_async_engine(
    "sqlite+aiosqlite:///tasks.db"
)

new_session = async_sessionmaker(engine, expire_on_commit=False)


class Model(DeclarativeBase):
    pass


async def create_tables():
    async  with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)


async def delete_tables():
    async  with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)


class TaskOrm(Model):
   __tablename__ = "tasks"
   id: Mapped[int] = mapped_column(primary_key=True)
   name: Mapped[str]
   description: Mapped[str | None]


