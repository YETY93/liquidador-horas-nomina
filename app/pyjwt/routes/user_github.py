from fastapi import APIRouter
from pydantic import BaseModel
from requests import get
from app.pyjwt.middlewares.verify_token_route import VerifyTokenRoute


user_github = APIRouter(route_class=VerifyTokenRoute)

class UserGithub(BaseModel):
    country: str
    page: str

@user_github.post("/user/github")
def github_users(github: UserGithub):
    return get(f'https://api.github.com/search/users?q=location:"{github.country}"&page={github.page}').json()