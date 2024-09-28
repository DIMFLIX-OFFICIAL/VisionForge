from fastapi import HTTPException, status


username_exits_exc = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Username already registered"
)
login_data_exc = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Incorrect username or password",
    headers={"WWW-Authenticate": "Bearer"},
)
credentials_exc = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)
error_required_parameter = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="The required parameters are not found"
)
