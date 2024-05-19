from pydantic import BaseModel

class user(BaseModel):
    username: str
    password: str
    email: str
    profileName: str
    profileImg: str

class updateUser(BaseModel):
    username: None
    password: None
    email: None
    profileName: None
    profileImg: None