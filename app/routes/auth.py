from fastapi import APIRouter, Depends, HTTPException, Response, status
from fastapi.security import OAuth2PasswordRequestForm

from app.models import users
from app.auth import Authenticator
from app.auth.users import BaseAuthentication
from app.database.base_user import BaseUserDatabase
from app.common.user import ErrorCode


def get_auth_router(
    backend: BaseAuthentication,
    user_db: BaseUserDatabase[users.BaseUserDB],
    authenticator: Authenticator,
    requires_verification: bool = False,
) -> APIRouter:
    """Generate a router with login/logout routes for an authentication backend."""
    router = APIRouter()
    get_current_user = authenticator.current_user(
        active=True, verified=requires_verification
    )

    @router.post("/login")
    async def login(
        response: Response, credentials: OAuth2PasswordRequestForm = Depends()
    ):
        user = await user_db.authenticate(credentials)

        if user is None or not user.is_active:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=ErrorCode.LOGIN_BAD_CREDENTIALS,
            )
        if requires_verification and not user.is_verified:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=ErrorCode.LOGIN_USER_NOT_VERIFIED,
            )
        return await backend.get_login_response(user, response)

    if backend.logout:

        @router.post("/logout")
        async def logout(response: Response, user=Depends(get_current_user)):
            return await backend.get_logout_response(user, response)

    return router
