import motor.motor_asyncio
from fastapi import Request
from app.users import FastAPIUsers
from app.models import users
from app.auth import JWTAuthentication
from app.database.users_db import MongoDBUserDatabase
from httpx_oauth.clients.google import GoogleOAuth2
from app.database.mongodb import atlas_uri
from typing import Optional

DATABASE_URL = atlas_uri
SECRET = "SECRET"

google_oauth_client = GoogleOAuth2("CLIENT_ID", "CLIENT_SECRET")


class User(users.BaseUser, users.BaseOAuthAccountMixin):
    first_name: Optional[str]
    last_name: Optional[str]

class UserCreate(users.BaseUserCreate):
    first_name: str
    last_name: str

class UserUpdate(User, users.BaseUserUpdate):
    first_name: Optional[str]
    last_name: Optional[str]

class UserDB(User, users.BaseUserDB):
    first_name: str
    last_name: str


client = motor.motor_asyncio.AsyncIOMotorClient(
    DATABASE_URL, uuidRepresentation="standard"
)
db = client["COAG"]
collection = db["Users"]
user_db = MongoDBUserDatabase(UserDB, collection)


def on_after_register(user: UserDB, request: Request):
    print(f"User {user.id} has registered.")


def on_after_forgot_password(user: UserDB, token: str, request: Request):
    print(f"User {user.id} has forgot their password. Reset token: {token}")


def after_verification_request(user: UserDB, token: str, request: Request):
    print(f"Verification requested for user {user.id}. Verification token: {token}")


jwt_authentication = JWTAuthentication(
    secret=SECRET, lifetime_seconds=3600, tokenUrl="auth/jwt/login"
)

fastapi_users = FastAPIUsers(
    user_db,
    [jwt_authentication],
    User,
    UserCreate,
    UserUpdate,
    UserDB,
)
