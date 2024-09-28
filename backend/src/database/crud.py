from .db import DatabaseManager
from .cruds.users import UsersCRUD


class CRUD(UsersCRUD):
	def __init__(self, db_manager: DatabaseManager) -> None:
		self.db_manager = db_manager
