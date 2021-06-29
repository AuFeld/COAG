from fastapi import FastAPI
from app.routes.company_routes import AtlasAPI
from mangum import Mangum
from app.database.utils import setup_mongodb
# from app.common.middlewares import StateRequestIDMiddleware
# from app.tracing.middlewares import OpentracingMiddleware
# from app.tracing.utils import setup_opentracing 
# from app.exception_handlers import setup_exception_handlers
from app.user_conf import (
    fastapi_users, jwt_authentication, on_after_register, SECRET, 
    on_after_forgot_password, after_verification_request, google_oauth_client )
from app.tags import tags_metadata
from starlette.middleware.cors import CORSMiddleware

app = FastAPI(
    fastapi_users=fastapi_users,
    openapi_tags=tags_metadata,
    title="COAG",
    description="A data driven application for career opportunities and growth"
)

'''
MongoDB Conn & Config at Startup w/ Middleware
'''

@app.on_event('startup')
async def startup():
    setup_mongodb(app)
    # adapter for AWS Lambda + API Gateway
    app.add_middleware(
    CORSMiddleware,
    allow_origins='*',
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

'''
Routes
'''

@app.get("/", tags=["Root"])
async def root():
    return {"message": "Welcome to COAG!"}
    
app.include_router(AtlasAPI, tags=["Atlas"], prefix="/growjo")
app.include_router(
    fastapi_users.get_auth_router(jwt_authentication), prefix="/auth/jwt", tags=["Auth"]
)
app.include_router(
    fastapi_users.get_register_router(on_after_register), prefix="/auth", tags=["Auth"]
)
app.include_router(
    fastapi_users.get_reset_password_router(
        SECRET, after_forgot_password=on_after_forgot_password
    ),
    prefix="/auth",
    tags=["Auth"],
)
app.include_router(
    fastapi_users.get_verify_router(
        SECRET, after_verification_request=after_verification_request
    ),
    prefix="/auth",
    tags=["Auth"],
)
app.include_router(fastapi_users.get_users_router(), prefix="/users", tags=["Users"])

google_oauth_router = fastapi_users.get_oauth_router(
    google_oauth_client, SECRET, after_register=on_after_register
)
app.include_router(google_oauth_router, prefix="/auth/google", tags=["Auth"])

'''
AWS Handler
'''

handler = Mangum(app)