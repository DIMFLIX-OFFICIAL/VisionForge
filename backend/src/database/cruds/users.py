from datetime import datetime
from typing import List, Optional
from sqlalchemy.future import select

from ..db import DatabaseManager
from ..models import User


class UsersCRUD:
	db_manager: DatabaseManager

	async def create_user(self, username: str, name: str, email: str, hashed_password: str) -> User:
		async with self.db_manager.get_session() as session:
			existing_user = await session.execute(select(User).where(User.username == username))
			existing_user = existing_user.scalar()

			if existing_user:
				await session.commit()
				return existing_user
	
			new_user = User(
				username=username, 
				name=name, 
				email=email, 
				hashed_password=hashed_password
			)

			session.add(new_user)
			await session.commit()
			await session.refresh(new_user)
			return new_user
		
	async def get_user_by_username(self, username: str) -> Optional[User]:
		async with self.db_manager.get_session() as session:
			result = await session.execute(select(User).where(User.username == username))
			return result.scalars().first() 
	
	async def update_refresh_token_by_username(self, username: str, refresh_token: str) -> None:
		async with self.db_manager.get_session() as session:
			user = await session.execute(select(User).where(User.username == username))
			user = user.scalar()
			user.refresh_token = refresh_token
			await session.commit()
			