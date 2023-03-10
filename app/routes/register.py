from typing import Callable, Optional, Type, cast

from fastapi import APIRouter, HTTPException, Request, status

from app.models import users
from app.common.user import ErrorCode, run_handler
from app.users.user import (
    CreateUserProtocol,
    InvalidPasswordException,
    UserAlreadyExists,
    ValidatePasswordProtocol,
)


def get_register_router(
    create_user: CreateUserProtocol,
    user_model: Type[users.BaseUser],
    user_create_model: Type[users.BaseUserCreate],
    after_register: Optional[Callable[[users.UD, Request], None]] = None,
    validate_password: Optional[ValidatePasswordProtocol] = None,
) -> APIRouter:
    """Generate a router with the register route."""
    router = APIRouter()

    @router.post(
        "/register", response_model=user_model, status_code=status.HTTP_201_CREATED
    )
    async def register(request: Request, user: user_create_model):  # type: ignore
        user = cast(users.BaseUserCreate, user)  # Prevent mypy complain
        if validate_password:
            try:
                await validate_password(user.password, user)
            except InvalidPasswordException as e:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail={
                        "code": ErrorCode.REGISTER_INVALID_PASSWORD,
                        "reason": e.reason,
                    },
                )

        try:
            created_user = await create_user(user, safe=True)
        except UserAlreadyExists:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=ErrorCode.REGISTER_USER_ALREADY_EXISTS,
            )

        if after_register:
            await run_handler(after_register, created_user, request)

        return created_user

    return router
