from pydantic import BaseModel
from dataclasses import dataclass
from typing import Optional

from src.database.models import User


class Register(BaseModel):
    email: str
    username: str
    password: str
    name: str


class Login(BaseModel):
    username: str
    password: str


class RefreshToken(BaseModel):
    refresh_token: str


@dataclass
class UpdatedTokens:
	access_token: str
	refresh_token: str
     

@dataclass
class IsAuthenticated:
	is_authenticated: bool
	user: Optional[User]
	access_token: Optional[str]
	refresh_token: Optional[str]
