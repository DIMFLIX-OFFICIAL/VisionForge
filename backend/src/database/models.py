from sqlalchemy import Column, Integer, BIGINT, TIMESTAMP, String, ForeignKey
from datetime import datetime
from typing import Any

from .db import Base


class User(Base):
	__tablename__ = 'users'
	username = Column(String, nullable=False, primary_key=True)
	name = Column(String, nullable=False)
	email = Column(String, nullable=False, default=0)
	hashed_password = Column(String, nullable=False)
	refresh_token = Column(String, nullable=True)
	created_at = Column(TIMESTAMP, nullable=False, default=datetime.now)

	def to_dict(self) -> dict[str, Any]:
		return {
			'username': self.username,
			'name': self.name,
			'email': self.email,
			'hashed_password': self.hashed_password,
			'refresh_token': self.refresh_token,
			'created_at': self.created_at,
		}
	