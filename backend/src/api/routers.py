from typing import Callable
from fastapi.routing import APIRoute
from fastapi import APIRouter, Request, Response

from src.loader import oauth2
from .errors import credentials_exc


class CustomAPIRoute(APIRoute):
	def get_route_handler(self) -> Callable:
		handler = super().get_route_handler()

		async def check_auth(request: Request) -> Response:
			access_token = request.cookies.get('access_token', None)
			refresh_token = request.cookies.get('refresh_token', None)
			is_authenticated = await oauth2.check_and_update_auth(access_token, refresh_token)

			if is_authenticated.is_authenticated:
				request.state.user = is_authenticated.user
				response = await handler(request)
				response.set_cookie(key="access_token", value=is_authenticated.access_token, httponly=True)
				response.set_cookie(key="refresh_token", value=is_authenticated.refresh_token, httponly=True)
				return response
			else:
				raise credentials_exc

		return check_auth


unprotected = APIRouter()
protected = APIRouter(prefix="/protected", route_class=CustomAPIRoute)
