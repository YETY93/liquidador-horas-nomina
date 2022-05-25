from fastapi import FastAPI
from dotenv import load_dotenv
from app.pyjwt.routes.auth import auth_routes
from app.pyjwt.routes.user_github import user_github

app= FastAPI()
app.include_router(auth_routes, prefix="/api/v1")
app.include_router(user_github, prefix="/api/v1")

env_path = "./app/temp/.env"
load_dotenv(dotenv_path=env_path)

