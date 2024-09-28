from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from contextlib import asynccontextmanager


class DatabaseManager:
    def __init__(self, database_url):
        self.engine = create_async_engine(database_url, echo=False)
        self.AsyncSession = sessionmaker(
            bind=self.engine, expire_on_commit=False, class_=AsyncSession
        )

    @asynccontextmanager
    async def get_session(self):
       async with self.AsyncSession() as session:
           try:
               yield session
           except Exception:
               await session.rollback()
               raise
           finally:
               await session.close()


Base = declarative_base()
