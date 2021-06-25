"""Ready-to-use and customizable users management for FastAPI."""

__version__ = "6.1.0"

from app.models import users  # noqa: F401
from app.users.fastapi_users import FastAPIUsers  # noqa: F401
from app.users.user import InvalidPasswordException  # noqa: F401
