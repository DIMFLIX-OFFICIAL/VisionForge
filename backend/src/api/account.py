import json
from fastapi import Request
from fastapi.responses import JSONResponse

from src.utils.json_custom_encoder import JSONCustomEncoder
from .routers import protected


@protected.post("/get_my_account_info")
async def get_my_account_info(request: Request):
    user = request.state.user.to_dict()
    del user["hashed_password"]
    del user["refresh_token"]
    return JSONResponse(json.dumps(user, cls=JSONCustomEncoder))
