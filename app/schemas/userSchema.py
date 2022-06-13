from pydantic import BaseModel


class User(BaseModel):
    id: int
    user_nickname: str
    user_firts_name: str
    user_other_name: str
    user_firts_lastname: str
    user_other_lastname: str
    user_rol: str
    state: int

    class Config:
        orm_mode = True
