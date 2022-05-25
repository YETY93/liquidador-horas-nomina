from fastapi import APIRouter, Header
from fastapi.responses import JSONResponse
from pydantic import BaseModel, EmailStr
from app.pyjwt.functions_jwt.functions_jwt import write_token, validate_token

auth_routes = APIRouter()


class User(BaseModel):
    userName: str
    email: EmailStr


@auth_routes.post("/login")
def login(user: User):
    print(user.dict())
    if user.userName == "Yesid Rangel":
        return write_token(user.dict())
    else:
        return JSONResponse(content={"message": "User not found"}, status_code=404)


@auth_routes.post("/verify/token")
def verify_token(Authorization: str = Header(None)):
    token = Authorization.split(" ")[1]
    token_decode = validate_token(token, output=True)
    return token_decode
