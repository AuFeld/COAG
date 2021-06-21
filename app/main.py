from fastapi import FastAPI
from app.routes.company_routes import AtlasAPI
#from app.oauth import OAuth as OAuthRouter
from mangum import Mangum
from app.database.utils import setup_mongodb
from app.common.middlewares import StateRequestIDMiddleware
from app.tracing.middlewares import OpentracingMiddleware
from app.tracing.utils import setup_opentracing 
from app.exception_handlers import setup_exception_handlers

tags_metadata = [
    {
        "name": "Atlas",
        "description": "Router for Growjo data",
        "externalDocs": {
            "description": "Growjo URL",
            "url": "https://wwww.growjo.com/",
        },
    },
        {
            "name": "Root",
            "description": "Base API",
        },
]

app = FastAPI(
    openapi_tags=tags_metadata,
    title="COAG",
    description="A data driven application for career opportunities and growth"
)
# mongodb connection at startup + config
@app.on_event('startup')
async def startup():
    setup_mongodb(app)
    app.add_middleware(StateRequestIDMiddleware)
    setup_opentracing(app)
    app.add_middleware(OpentracingMiddleware)
    setup_exception_handlers(app)

# routers
app.include_router(AtlasAPI, tags=["Atlas"], prefix="/growjo")

# router for oauth
#app.include_router(OAuthRouter)

@app.get("/", tags=["Root"])
async def root():
    return {"message": "Welcome to COAG!"}


handler = Mangum(app)